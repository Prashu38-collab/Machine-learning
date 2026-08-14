import pandas as pd 

df=pd.read_csv("test_Data.csv")
print(df)

# Rows and columns selection = only specfic columns selection

print(df[["name"]])

# multiple columns 

print(df[["name","age"]])