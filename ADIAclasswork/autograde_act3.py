import pandas as pd

def load_dataset():
  # URL to the dataset (Example: January 2024 Yellow Taxi Data in Parquet format)
  url = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-01.parquet"

  # Read the dataset directly into a Pandas DataFrame
  df = pd.read_parquet(url).astype(str)
  return df

def grade_p1(globals):
  if "columns_float" not in globals:
    print("Error, the variable columns_float is not defined.")
    return
  columns_float = globals["columns_float"]
  if type(columns_float) != list:
    print("You should store a list in columns_float, defined using square brackets [] and separating items with commas.")
  passed = True
  columns_float_ans = ["passenger_count", "trip_distance", "RatecodeID", "fare_amount", "extra", "mta_tax", "tip_amount", "tolls_amount", "improvement_surcharge", "total_amount", "congestion_surcharge", "Airport_fee"]
  for col in columns_float_ans:
    if col not in columns_float:
      print(f"You forgot to include {col} in columns_float. ")
      passed = False

  if "columns_datetime" not in globals:
    print("Error, the variable columns_datetime is not defined.")
    return
  columns_datetime = globals["columns_datetime"]
  if type(columns_datetime) != list:
    print("You should store a list in columns_datetime, defined using square brackets [] and separating items with commas.")
  passed = True
  columns_datetime_ans = ["tpep_pickup_datetime", "tpep_dropoff_datetime"]
  for col in columns_datetime_ans:
    if col not in columns_datetime:
      print(f"You forgot to include {col} in columns_float. ")
      passed = False

  if passed:
    print("Well done! Now you can move on to the next section.")
  else:
    print("You should fix your code until you pass this section, because this will be required in the next part!")


def grade_p2(globals):
  if "df" not in globals:
    print("Error. The variable df is not defined. ")
    return
  df = globals["df"]
  if type(df) != pd.DataFrame:
    print("Error. The variable df should be a pandas DataFrame")
  columns_float_ans = ["passenger_count", "trip_distance", "RatecodeID", "fare_amount", "extra", "mta_tax", "tip_amount", "tolls_amount", "improvement_surcharge", "total_amount", "congestion_surcharge", "Airport_fee"]
  passed = True
  for col in columns_float_ans:
    if df.dtypes[col] != 'float64':
      passed = False
      print(f"You did not convert {col} to float.")
  if passed:
    print("Good job! You got it!")


def grade_p3(globals):
  if "df" not in globals:
    print("Error. The variable df is not defined. ")
    return
  df = globals["df"]
  if type(df) != pd.DataFrame:
    print("Error. The variable df should be a pandas DataFrame")
  columns_datetime_ans = ["tpep_pickup_datetime", "tpep_dropoff_datetime"]
  passed = True
  for col in columns_datetime_ans:
    if df.dtypes[col] != '<M8[ns]':
      passed = False
      print(f"You did not convert {col} to datetime.")
  if passed:
    print("Good job! You got it!")

def grade_p4(globals):
  if "num_rows" not in globals:
    print("Error, the variable num_rows is not defined")
    return
  if globals["num_rows"] != 2964624:
    print("Wrong answer, try again! ")
  else:
    print("You got it!")

def grade_p5(globals):
  if "passenger_count" not in globals:
    print("Error, the variable passenger_count is not defined")
    return
  if globals["passenger_count"] != 51:
    print("Wrong answer, try again! ")
  else:
    print("You got it!")

def grade_p6(globals):
  if "busiest_vendor" not in globals:
    print("Error, the variable busiest_vendor is not defined")
    return
  if globals["busiest_vendor"] != 2:
    print("Wrong answer, try again! ")
  else:
    print("You got it!")

def grade_p7(globals):
  if "longest_trip" not in globals:
    print("Error, the variable longest_trip is not defined")
    return
  if globals["longest_trip"] != 312722.3:
    print("Wrong answer, try again! ")
  else:
    print("You got it!")

def grade_p8(globals):
  if "largest_fare" not in globals:
    print("Error, the variable largest_fare is not defined")
    return
  if globals["largest_fare"] != 5000:
    print("Wrong answer, try again! ")
  else:
    print("You got it!")


def grade_p9(globals):
  if "cheapest_ride" not in globals:
    print("Error, the variable cheapest_ride is not defined")
    return
  if globals["cheapest_ride"] != -899.0:
    print("Wrong answer, try again! ")
  else:
    print("You got it! Your code is correct, though it seems the dataset may contain some errors worth cleaning...")
    print("A little teaser for what's to come and why it matters. ")
