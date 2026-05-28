import pandas as pd
import math

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

  df_clean = df_clean.sample(n=100000, random_state=42)

  
  return df_clean


def grade_p1(globals):
  var = "passenger_count_with_highest_mean_duration"
  if var not in globals:
    print(f"Error. The variable {var} is not defined. Did you run the cell above?")
    return
  else:
    var = globals[var]
  if var == 6:
    print(f"Great! Your answer for {var} is correct!")
  else:
    print("Not quite... read your grouped data again!")

  var = "passenger_count_highest_mean_duration"
  if var not in globals:
    print(f"Error. The variable {var} is not defined. Did you run the cell above?")
    return
  else:
    var = globals[var]
  if math.isclose(var, 21.046109, abs_tol=0.1):
    print(f"Great! Your answer for {var} is correct!")
  else:
    print("Not quite... read your grouped data again!")

  var = "passenger_count_with_highest_fare_mean"
  if var not in globals:
    print(f"Error. The variable {var} is not defined. Did you run the cell above?")
    return
  else:
    var = globals[var]
  if var==8:
    print(f"Great! Your answer for {var} is correct!")
  else:
    print("Not quite... read your grouped data again!")


def grade_p2(globals):
  var = "total_trips_vendor1"
  if var not in globals:
    print(f"Error. The variable {var} is not defined. Did you run the cell above?")
    return
  else:
    var = globals[var]
  if var == 23757:
    print(f"Great! Your answer for {var} is correct!")
  else:
    print("Not quite... read your grouped data again!")

  var = "total_fare_vendor2"
  if var not in globals:
    print(f"Error. The variable {var} is not defined. Did you run the cell above?")
    return
  else:
    var = globals[var]
  if math.isclose(var, 1432182.70, abs_tol=0.1):
    print(f"Great! Your answer for {var} is correct!")
  else:
    print("Not quite... read your grouped data again!")

  var = "highest_var_vendor"
  if var not in globals:
    print(f"Error. The variable {var} is not defined. Did you run the cell above?")
    return
  else:
    var = globals[var]
  if var==2:
    print(f"Great! Your answer for {var} is correct!")
  else:
    print("Not quite... read your grouped data again!")

def grade_p3(globals):
  var = "friday_most_frequent_hour"
  if var not in globals:
    print(f"Error. The variable {var} is not defined. Did you run the cell above?")
    return
  else:
    var = globals[var]
  if var == 18:
    print(f"Great! Your answer for {var} is correct!")
  else:
    print("Not quite... read your grouped data again!")

def grade_p4(globals):
  var = "trips_friday_22"
  if var not in globals:
    print(f"Error. The variable {var} is not defined. Did you run the cell above?")
    return
  else:
    var = globals[var]
  if var == 805:
    print(f"Great! Your answer for {var} is correct!")
  else:
    print("Not quite... read your grouped data again!")

def grade_p5(globals):
  var = "passenger_count_6_weekday"
  if var not in globals:
    print(f"Error. The variable {var} is not defined. Did you run the cell above?")
    return
  else:
    var = globals[var]
  if var == "Wednesday":
    print(f"Great! Your answer for {var} is correct!")
  else:
    print("Not quite... read your grouped data again!")
