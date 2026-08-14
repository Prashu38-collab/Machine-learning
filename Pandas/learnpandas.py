import pandas as pd
df=pd.DataFrame([11,12,13],columns=["Col_name"])
print(df)

data={
    "name": ["prashamsa","prashu","riya","siya","ram"],
    "age":[21,22,23,24,25],
    "salary":[344444,1234,32322,1234,12343]
}
df=pd.DataFrame(data=data)
print(type(df))

print(df.head(2))
print(df.tail(3))
print(df.shape)
print(df.columns)
# rename columns
df.rename(columns={"salary":"Monthly_Salary"},inplace=True)
print(df)
df.info()
print(df.describe())

# to save data
df.to_csv("test_Data.csv",index=False)