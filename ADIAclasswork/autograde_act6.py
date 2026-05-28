import pandas as pd

def load_data():
  df_sol = load_dataset()
  df_sol["trip_distance_km"] = df_sol["trip_distance"]* 1.60934
  df_sol["tip_percentage"] = (df_sol["tip_amount"]/df_sol["fare_amount"])*100
  df_sol["trip_duration"] = (df_sol["tpep_dropoff_datetime"] - df_sol["tpep_pickup_datetime"]).dt.total_seconds()/60
  df_sol["hour_start"] = df_sol["tpep_pickup_datetime"].dt.hour
  df_sol["weekday"] = df_sol["tpep_pickup_datetime"].dt.day_name()
  df_sol["average_speed"] = df_sol["trip_distance_km"]/(df_sol["trip_duration"]/60)
  df_sol["length_category"] = df_sol["trip_distance_km"].apply(categorize_length_sol)
  df_sol["time_of_day"] = df_sol["hour_start"].apply(categorize_time_of_day_sol)
  df_sol.reset_index(drop=True, inplace=True)
  df_sol["tpep_dropoff_datetime"] = df_sol["tpep_dropoff_datetime"].astype("datetime64[ns]")
  df_sol["tpep_pickup_datetime"] = df_sol["tpep_pickup_datetime"].astype("datetime64[ns]")
  int_cols = ["VendorID", "PULocationID", "DOLocationID", "hour_start"]
  for col in int_cols:
      df_sol[col] = df_sol[col].astype("int64")
  ### Sampling to keep only 10% of the data: 
  # df_sol = df_sol.sample(frac=0.1, random_state=1234)
  return df_sol


def load_dataset():
  # URL to the dataset (Example: January 2024 Yellow Taxi Data in Parquet format)
  url = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-01.parquet"

  # Read the dataset directly into a Pandas DataFrame
  df = pd.read_parquet(url)
  df_clean = df.dropna()
  df_clean = df_clean[df_clean["passenger_count"]>0]
  df_clean = df_clean[df_clean["trip_distance"]>0]
  df_clean = df_clean[df_clean["fare_amount"]>0]
  df_clean = df_clean[df_clean["tip_amount"]>=0]
  df_clean = df_clean[df_clean["total_amount"]>0]

  
  return df_clean
def categorize_length_sol(length):
  if length > 5:
    return "long"
  else:
    return "short"

def categorize_time_of_day_sol(hour):
  if hour < 6:
    return "late night"
  elif hour < 12:
    return "morning"
  elif hour < 21:
    return "afternoon"
  else:
    return "night"
    

def make_solution():
  df_sol = load_dataset()
  df_sol["trip_distance_km"] = df_sol["trip_distance"]* 1.60934
  df_sol["tip_percentage"] = (df_sol["tip_amount"]/df_sol["fare_amount"])*100
  df_sol["trip_duration"] = (df_sol["tpep_dropoff_datetime"] - df_sol["tpep_pickup_datetime"]).dt.total_seconds()/60
  df_sol["hour_start"] = df_sol["tpep_pickup_datetime"].dt.hour
  df_sol["weekday"] = df_sol["tpep_pickup_datetime"].dt.day_name()
  df_sol["average_speed"] = df_sol["trip_distance_km"]/(df_sol["trip_duration"]/60)
  df_sol["length_category"] = df_sol["trip_distance_km"].apply(categorize_length_sol)
  df_sol["time_of_day"] = df_sol["hour_start"].apply(categorize_time_of_day_sol)
  df_sol.reset_index(drop=True, inplace=True)
  df_sol["tpep_dropoff_datetime"] = df_sol["tpep_dropoff_datetime"].astype("datetime64[ns]")
  df_sol["tpep_pickup_datetime"] = df_sol["tpep_pickup_datetime"].astype("datetime64[ns]")
  int_cols = ["VendorID", "PULocationID", "DOLocationID", "hour_start"]
  for col in int_cols:
      df_sol[col] = df_sol[col].astype("int64")
  df_sol = df_sol.sample(frac=0.1, random_state=1234)
  df_sol.reset_index(inplace=True, drop=True)
  return df_sol


df_sol = make_solution()

def grade_p1(globals):
  if "df" not in globals:
    print("Error. Did you load the DataFrame into a variable called 'df'?")
    return
  else:
    df = globals["df"]
  if df.columns.equals(df_sol.columns):
    print("Columns are ok.")
  if df.index.equals(df_sol.index):
    print("I")
  if df.dtypes.equals(df_sol.dtypes):
    print("dtypes are ok")
  if df.columns.equals(df_sol.columns) and df.index.equals(df_sol.index) and df.dtypes.equals(df_sol.dtypes):
    print("Great!")
  else:
    print("Error. You did not correctly load the dataframe. Did you convert the pickup and dropoff time columns into datetime objects? These are always read as strings when loading datasets!")

import math

def grade_p2(globals):
  if "trip_duration_55" not in globals:
    print("Error. You did not record your answer into the variable 'trip_duration_55'. Did you run the cell above?")
    return
  ans = df_sol.loc[55, "trip_duration"]
  if math.isclose(globals["trip_duration_55"], ans, abs_tol=0.1):
    print("Great!")
  else:
    print("Not quite... try again!")

def grade_p3(globals):
  if "data_80_5" not in globals:
    print("Error. You did not record your answer into the variable 'data_80_5'. Did you run the cell above?")
    return
  ans = df_sol.loc[55, "trip_duration"]
  if math.isclose(globals["trip_duration_55"], ans, abs_tol=0.1):
    print("Great!")
  else:
    print("Not quite... try again!")

def grade_p4(globals):
  if "inds_many_passengers" not in globals:
    print("Error. You did not record your answer into the variable 'inds_many_passengers'. Ddi you run the cell above?")
    return
  ans = df_sol[df_sol["passenger_count"] > 4].index
  if ans.equals(globals["inds_many_passengers"]):
    print("Good job!")
  else:
    print("Try again. Did you extract the indices as instructed?")
    

def grade_p5(globals):
  if "speed_first_many_passengers" not in globals:
    print("Error. You did not record your answer into the variable 'speed_first_many_passengers'. Ddi you run the cell above?")
    return
  ind = df_sol[df_sol["passenger_count"] > 4].index[0]
  ans = df_sol.loc[ind, "average_speed"]
  if math.isclose(globals["speed_first_many_passengers"], ans, abs_tol=0.1):
    print("Good job!")
  else:
    print("Try again. Did you extract the indices as instructed?")   


def grade_p6(globals):
  if "min_speed_index" not in globals:
    print("Error. You did not record your answer into the variable 'min_speed_index'. Ddi you run the cell above?")
    return
  ans = df_sol["average_speed"].idxmin()
  if math.isclose(globals["min_speed_index"], ans, abs_tol=0.1):
    print("Good job!")
  else:
    print("Try again. Did you extract the index of the minimum value of the column 'average_speed'?")   


def grade_p7(globals):
  if "max_speed_index" not in globals:
    print("Error. You did not record your answer into the variable 'max_speed_index'. Ddi you run the cell above?")
    return
  ans = df_sol["average_speed"].idxmax()
  if math.isclose(globals["max_speed_index"], ans, abs_tol=0.1):
    print("Good job!")
  else:
    print("Try again. Did you extract the index of the maximum value of the column 'average_speed'?")   


def grade_p8(globals):
  if "passengers_max_speed" not in globals:
    print("Error. You did not record your answer into the variable 'passengers_max_speed'. Ddi you run the cell above?")
    return
  max_speed_index = df_sol["average_speed"].idxmax()
  ans = df_sol.loc[max_speed_index, "passenger_count"]
  if math.isclose(globals["passengers_max_speed"], ans, abs_tol=0.1):
    print("Good job!")
  else:
    print("Try again. Did you extract the index of the maximum speed, and then use it to select the passenger_count column with .iloc?")   


def grade_p9(globals):
  if "num_speed_2_3" not in globals:
    print("Error. You did not record your answer into the variable 'num_speed_2_3'. Ddi you run the cell above?")
    return
  ans = df_sol[(df_sol["average_speed"]>2) & (df_sol["average_speed"]<3)].shape[0]
  if math.isclose(globals["num_speed_2_3"], ans, abs_tol=0.1):
    print("Good job!")
  else:
    print("Try again. Did you combine conditions using & and apply .shape to analyze how many rows were in the filtered DataFrame, or add the booleans of the combined masks using .sum()?")


def grade_p10(globals):
  if "mean_fare_vendor1" not in globals:
    print("Error. You did not record your answer into the variable 'mean_fare_vendor1'. Ddi you run the cell above?")
    return
  ans = df_sol[(df_sol["VendorID"] == 1) & (df_sol["trip_distance_km"] >= 3)]["fare_amount"].mean()
  if math.isclose(globals["mean_fare_vendor1"], ans, abs_tol=0.1):
    print("Good job!")
  else:
    print("Try again. Did you combine the proper conditions, then select the 'fare_amount' column and finnally apply the .mean() method?")










