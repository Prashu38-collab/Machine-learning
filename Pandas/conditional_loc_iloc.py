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

# Select everyone whose age is greater than 22.
print(df.loc[df["age"]>22])

# Select everyone whose score is greater than 80.
print(df.loc[df["score"]>80])

# Select everyone from Kathmandu.
print(df.loc[df["city"]=='Kathmandu'])

# Select everyone from the IT department.
print(df.loc[df["department"]=='IT'])

# Select everyone whose age is exactly 21.
print (df.loc[df["age"]==21])

# Select only the names and score of people whose score is greater than 85.

print(df.loc[df["score"]>85,["name","score"]])

# Select name, city, and department for everyone from Kathmandu.

print(df.loc[df["city"]=="Kathmandu",["name","city","department"]])


# Multiple conditions

#  Find people who:

# age > 21 AND score > 85

#  Return all columns.

print(df.loc[(df["age"]>21) & (df["score"]>85)])

# Find people who:

# age >= 21 AND age <= 24

print(df.loc[(df["age"]>=21) & (df["age"]<=24)])

# Find people who:

# score > 80 AND department == "IT"

print(df.loc[(df["score"]>80) & (df["department"]=='IT')])

# Find people who:

# department == "CS" OR department == "IT"

print(df.loc[(df["department"]=="CS") | (df["department"]=="IT")])

# Find people who are from Kathmandu OR Pokhara.
print(df.loc[(df["city"]=="Kathmandu") | (df["city"]=="Pokhara")])

# Find people whose score is greater than 80 AND whose city is Kathmandu.

# Return only:

# name
# score
# city

print(df.loc[(df["score"]>80) & (df["city"]=="Kathmandu"),["name","score","city"]])

# using loc for modifying data

# Change Ram's score from 70 to 80.

df.loc[df["name"]=="Ram","score"]= 80
print(df.loc[df["name"] == "Ram"])

# Change Mina's age from 25 to 26.

df.loc[df["name"]=="Mina","age"]=26
print(df.loc[df["name"]=="Mina"])

# Change Gita's department from "Management" to "IT".

df.loc[df["name"]=="Gita","department"]='IT'
print(df.loc[df["name"]=="Gita"])

# Increase the score of everyone with a score below 70 to 70.
df.loc[df["score"]<70,"score"]=70
print(df.loc[df["name"] == "Bikash", "score"])

# Add 5 points to everyone in the IT department.

df.loc[df["department"]=="IT","score"]=+5

# Change the city of everyone from Lalitpur to Kathmandu.
df.loc[df["city"]=="Lalitpur","city"]="Kathmandu"

# Set the score to 100 for anyone whose current score is greater than 90.

df.loc[df["score"]>90,"score"]=100

print(df.loc[df["name"]=="Mina"])

print(df.iloc[3, 3])