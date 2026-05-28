import pandas as pd 

def load_orders():
  df1 = pd.read_csv("ADIAclasswork/orders1.csv", index_col="Unnamed: 0")
  df2 = pd.read_csv("ADIAclasswork/orders2.csv", index_col="Unnamed: 0")
  return df1, df2

def load_customers():
  df1 = pd.read_csv("ADIAclasswork/customers1.csv", index_col="Unnamed: 0")
  df2 = pd.read_csv("ADIAclasswork/customers2.csv", index_col="Unnamed: 0")
  return df1, df2

def load_products():
  df = pd.read_csv("ADIAclasswork/olist_products_dataset.csv")
  return df

def load_reviews():
  df = pd.read_csv("ADIAclasswork/olist_order_reviews_dataset.csv")
  return df

def load_order_items():
  df = pd.read_csv("ADIAclasswork/olist_order_items_dataset.csv")
  return df


  
