import pandas as pd

df = pd.DataFrame({
    "name": ["Ram", "Sita", "Hari", "Gita", "Aarav", "Nisha", "Bikash", "Mina"],
    "age": [20, 21, 22, 20, 24, 23, 21, 25],
    "city": [
        "Kathmandu", "Pokhara", "Lalitpur", "Bhaktapur",
        "Kathmandu", "Pokhara", "Lalitpur", "Kathmandu"
    ],
    "score": [70, 85, 90, 75, 88, 92, 65, 95],
    "department": [
        "IT", "CS", "IT", "Management",
        "CS", "IT", "Management", "CS"
    ]
})

print(df)

# Basic loc
# Get the row with index 3.

print(df.loc[3])

# Get the row with index 5.
print(df.loc[5])

# Get the name of person with index 2.

print(df.loc[2,"name"])

# Get the score and name of the person at index 6.
print(df.loc[6,["score","name"]])

# Get the age of Mina.

age=df.loc[df["name"]=="Mina","age"].item()
print(age)

# Get the entire name column using loc.

print(df.loc[:,"name"])

# Get the entire score column using loc.

print(df.loc[:,"score"])

# Get the name and city columns for everyone.
print(df.loc[:,["name","city"]])

# Get the name, age, and score columns for everyone.

print(df.loc[:,["name","score","city"]])

# Get rows with indexes 1, 3, and 6.
print(df.loc[[1,3,6]])

# practise for iloc
print(df.iloc[0])

# Get the fourth row using iloc.
print(df.iloc[3])

# Get the first column using iloc.
print(df.iloc[:,0])

# Get the value at row position 2, column position 3.
print(df.iloc[2,2])
# in loc we need to specify column label to get the value
print(df.loc[2,"city"])

# Get the value at row position 5, column position 1.

print(df.iloc[5,1])

# Get the first three rows.

print(df.iloc[0:3])

# Get the last three rows.
print(df.iloc[-3:])

# Get rows at positions 0, 3, and 6.
print(df.iloc[[0,3,6]])

# Get columns at positions 0, 2, and 4.
print(df.iloc[:,[0,2,4]])

