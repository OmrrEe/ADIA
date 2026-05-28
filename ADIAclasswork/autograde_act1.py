### Autograde Act1

import pandas as pd

def grade_p1(globals):
    ### Check that the variables "names" and "ages" are defined
    if "names" not in globals:
        print("Error! Did you store your names Series into a variable called 'names'? You may have forgotten to run the code in the cell above")
        return 
    if "ages" not in globals:
        print("Error! Did you store your ages Series into a variable called 'ages'?")
        return
    if "heights" not in globals:
        print("Error! Did you store your heights Series into a variable called 'heights'?")
        return
    
    names = globals["names"]
    ages = globals["ages"]
    heights = globals["heights"]
    passed = True
    if type(names) != pd.core.series.Series:
        print("Error! The variable 'names' must be a pandas Series. It appears to be something else.")
        passed = False
    if type(ages) != pd.core.series.Series:
        print("Error! The variable 'ages' must be a pandas Series. It appears to be something else.")
        passed = False
    if type(heights) != pd.core.series.Series:
        print("Error! The variable 'heights' must be a pandas Series. It appears to be something else.")
        passed = False
    if names.dtype != "O":
        print("Error! The values in your 'names' series should be text!" )
        passed = False
    if ages.dtype != "int64":
        print("Error! The values in your 'ages' series should be integers! Make sure you used only whole numbers.")
        passed = False
    if heights.dtype != "float64":
        print("Error! The values in your 'height' series should be floats! Make sure you used numbers with decimal placemests.")
        passed = False 
    if len(names) < 3:
        print("Error! Your names series should contain at least 3 names. ")
        passed = False
    if len(ages) < 3:
        print("Error! Your ages series must contain at least 3 ages.")
        passed = False
    if len(heights) < 3:
        print("Error! Your heights series must contain at least 3 heights.")
        passed = False
    if len(names) != len(ages) and len(ages) != len(heights):
        print("Your names, ages and heights series should be of the same length. You must record the name and age of each theoretical person.")
        passed = False
    
    if names.name != 'Name':
        print("You forgot to specify the name of the names Series. Make sure to use 'name='Name'' when creating the series!")
        passed = False
    if ages.name != "Age":
        print("You forgot to specify the name of the Age series. Make sure to use 'name='Age'' when creating the series!")
        passed = False
    if heights.name != "Height":
        print("You forgot to specify the name of the Height series. Make sure to use 'name='Height'' when creating the series!")
        passed = False
    if passed:
        print("Congratulations! You passed this part of the assignment. Time to move to the next one. ")
    
def grade_p2(globals):
    if "my_dataframe" not in globals:
        print("Error! Did you store your DataFrame in a variable called 'my_dataframe'?")
        return 
    my_df = globals["my_dataframe"]

    passed = True
    if len(my_df) < 3:
        print("Error! Your DataFrame should contain at least 3 rows or data points.")
        passed = False
    
    if not my_df.dtypes.eq("object").any():
        print("Error! Your DataFrame doesn't contain a column of Data Type object. Make sure you include a text column. ")
        passed = False
    if not my_df.dtypes.eq("int64").any():
        print("Error! Your DataFrame doesn't contain a column of Data Type int64. Make sure you include a whole number column.")
        passed = False
    if not my_df.dtypes.eq("float64").any():
        print("Error! Your DataFrame doesn't contain a column of Data Type float64. Make sure you include a column with decimal values.")  
        passed = False

    if passed:
        print("Congratulations! You passed this part of the assignment. Great job!")
