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
# Using loc, select rows from index 2 through index 5.

# key point: loc will not exclude the last value while performing slicing whereas iloc will exlcude the last value

print(df.loc[2:5])
print(df.iloc[2:5])

# Using loc, select rows 1 through 4 and only the name and score columns.

print(df.loc[1:4,["name","score"]])

# Using iloc, select rows positions 1 through 4 and columns positions 0 through 3.

print(df.iloc[1:4,0:3])

# Using loc, select indexes 0 through 6 and columns age, city, and score.

print(df.loc[0:6,["age","city","score"]])

# Using iloc, select the first 5 rows and last 2 columns.

print(df.iloc[0:5,-2:])