import pandas as pd

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
  return df_sol


df_sol = make_solution()

def grade_p1(globals):
  df = globals["df"]
  if "trip_distance_km" not in df.columns:
    print("Error. Did you name the column 'trip_distance_km' as expected?")
  elif df_sol['trip_distance_km'].equals(df['trip_distance_km']):
    print("Great job!")
  else:
    print("Are you sure you used the full 1.60934 to convert miles to kilometers?")


def grade_p2(globals):
  name = "tip_percentage"
  df = globals["df"]
  if name not in df.columns:
    print(f"Error. Did you name the column '{name}' as expected?")
  elif df_sol[name].equals(df[name]):
    print("Great job!")
  else:
    print("Your results are not right... Did you multiply by 100?")


def grade_p3(globals):
  name = "trip_duration"
  df = globals["df"]
  if name not in df.columns:
    print(f"Error. Did you name the column '{name}' as expected?")
  elif df_sol[name].equals(df[name]):
    print("Great job!")
  else:
    print("Your results are not right... Did you divide by 60 after obtaining the total seconds using dt.total_seconds()?")

def grade_p4(globals):
  name = "hour_start"
  df = globals["df"]
  if name not in df.columns:
    print(f"Error. Did you name the column '{name}' as expected?")
  elif df_sol[name].equals(df[name]):
    print("Great job!")
  else:
    print("Your results are not right... Did you use dt.hour?")

def grade_p5(globals):
  name = "weekday"
  df = globals["df"]
  if name not in df.columns:
    print(f"Error. Did you name the column '{name}' as expected?")
  elif df_sol[name].equals(df[name]):
    print("Great job!")
  else:
    print("Your results are not right... Did you use dt.day_name()?")

def grade_p6(globals):
  name = "average_speed"
  df = globals["df"]
  if name not in df.columns:
    print(f"Error. Did you name the column '{name}' as expected?")
  elif df_sol[name].equals(df[name]):
    print("Great job!")
  else:
    print("Your results are not right... Did you divide trip_duration by 60?")

def grade_p7(globals):
  name = "length_category"
  df = globals["df"]
  if name not in df.columns:
    print(f"Error. Did you name the column '{name}' as expected?")
  elif df_sol[name].equals(df[name]):
    print("Great job!")
  else:
    print("Your results are not right... Did you properly define your categoriging function and use .apply()?")

def grade_p8(globals):
  name = "time_of_day"
  df = globals["df"]
  if name not in df.columns:
    print(f"Error. Did you name the column '{name}' as expected?")
  elif df_sol[name].equals(df[name]):
    print("Great job!")
  else:
    print("Your results are not right... Did you properly define your categoriging function and use .apply()?")
