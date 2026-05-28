import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import shapiro, normaltest, anderson, probplot, mstats

import pandas as pd

def load_data_fbg():
  df = pd.read_csv("ADIAclasswork/blood_glucose.csv")
  return df

def load_data_height():
  df = pd.read_csv("ADIAclasswork/heights.csv")
  return df

def load_dataset_body():
  df = pd.read_csv("ADIAclasswork/body_measurements_clean.csv", index_col="Unnamed: 0")
  df.reset_index(inplace=True, drop=True)
  return df


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

  df_sol = df_sol[df_sol["trip_duration"]>0]
  df_sol = df_sol[df_sol["trip_duration"]<120]
  
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

  # df_clean = df_clean.sample(n=100000, random_state=42)
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

  df_clean = df_clean[df_clean["trip_distance"]<100]
  df_clean = df_clean[df_clean["fare_amount"]<100]


  
  return df_clean

def plot_hist_qq(df, column, bins=10, kde=True):
    data = df[column].dropna()
    # Visualization
    fig, ax = plt.subplots(1, 2, figsize=(12, 5))

    # Histogram + KDE
    sns.histplot(data, kde=kde, ax=ax[0], bins=bins)
    ax[0].set_title(f"Histogram of {column}")

    median = data.median()
    q1 = data.quantile(0.16)
    q11 = data.quantile(0.84)
    q2 = data.quantile(0.025)
    q22 = data.quantile(0.975)
    q3 = data.quantile(0.9965)
    q33 = data.quantile(0.0035)



    # Plot vertical lines
    ax[0].axvline(median, color='red', linestyle='-', label='Median')
    ax[0].axvline(q1, color='blue', linestyle='--', label='one sigma')
    ax[0].axvline(q11, color='blue', linestyle='--', label='one sigma')
    ax[0].axvline(q2, color='green', linestyle=':', label='2 sigma')
    ax[0].axvline(q22, color='green', linestyle=':', label='2 sigma')
    ax[0].axvline(q3, color='purple', linestyle=':', label='3 sigma')
    ax[0].axvline(q33, color='purple', linestyle=':', label='3 sigma')  
    # ax.axvline(z_neg1, color='purple', linestyle='-.', label='Z = -1')
    # ax.axvline(z_pos1, color='purple', linestyle='-.', label='Z = 1')

    # QQ-Plot
    probplot(data, dist="norm", plot=ax[1])
    ax[1].set_title(f"QQ-Plot of {column}")

    plt.show()
