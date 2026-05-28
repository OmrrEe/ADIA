import pandas as pd

def load_data():
  df = pd.read_csv("ADIAclasswork/data_missing.csv")
  return df
