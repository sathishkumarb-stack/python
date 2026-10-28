
import pandas as pd

# 1. Create employees.csv
csv_data = """id,name,department,salary,city
1,Arun,Sales,30000,Chennai
2,Priya,HR,45000,Chennai
3,Rahul,IT,60000,Bangalore
4,Divya,IT,75000,Chennai
5,Karthik,Finance,90000,Mumbai
6,Meena,Sales,52000,Bangalore
7,Suresh,IT,68000,Chennai
8,Anitha,HR,48000,Mumbai
"""

with open("employees.csv", "w") as file:
    file.write(csv_data)

# 2. Load the CSV file
df = pd.read_csv("employees.csv")

# 3. Explore the DataFrame
print("First 5 rows:")
print(df.head())

print("\nDataFrame information:")
df.info()

print("\nStatistical summary:")
print(df.describe())

# 4. Select columns
print("\nName column:")
print(df["name"])

print("\nName and salary:")
print(df[["name", "salary"]])

# 5. Select Chennai employees using loc
chennai = df.loc[df["city"] == "Chennai", "name"]

print("\nChennai employees:")
print(", ".join(chennai))

# 6. Select rows and columns using iloc
print("\nFirst 3 rows, columns 2 and 3:")
print(df.iloc[0:3, 1:3])

# 7. Filter employees with salary above 50000
high_salary = df[df["salary"] > 50000]

print("\nEmployees with salary above 50000:")
print(high_salary[["name", "salary"]])
print("Count:", len(high_salary))

# 8. Filter IT department employees
it_employees = df[df["department"] == "IT"]

print("\nIT department employees:")
print(", ".join(it_employees["name"]))
print("Count:", len(it_employees))
