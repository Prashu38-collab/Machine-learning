import pandas as pd 

df=pd.read_csv("test_Data.csv")
print(df)

# Rows and columns selection = only specfic columns selection

print(df[["name"]])

# multiple columns 

print(df[["name","age"]])

print(df.where(df['age']>=24))

print(df.where(df['age']>=24,other="Not eligible"))

# to add new column and row 
# adding new columm
df["Team"]=["CEO","CTO","HR","CDO","CMO"]
print(df)

df['Bonus']=df["Monthly_Salary"]*0.2
print(df)

# adding new row 
df.loc[len(df)]=['basu',26,233323,'CDO',352]
print(df)

# update value
df.loc[1,'Monthly_Salary']=12345
print(df)

df.loc[df["name"]=="siya","Monthly_Salary"]=123456
print(df)
# dropping row
df.drop(df[df.name =="siya"].index,inplace=True)
print(df)


print(df)

df["DOJ"]=["2024-09-29","2023-09-09","2022-08-03","2012-09-03","2022-09-07"]
print(df)
# current data type of doj is obect
print(df['DOJ'].dtype)
# changing to datetime
df['DOJ']=pd.to_datetime(df['DOJ'])

print(df['DOJ'].dtype)
print(df['DOJ'].dt.year)

# Handling Missing values
print(df.isnull())

# Aggregation and Group by 

print(df['Team'].value_counts)