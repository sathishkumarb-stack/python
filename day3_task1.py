
import pandas as pd
from io import StringIO

# Create orders.csv data
csv_data = """order_id,customer_id,amount
1,101,500
2,102,
3,101,700
3,101,700
4,103,300
5,104,900
"""

with open("orders.csv", "w") as file:
    file.write(csv_data)

# Load the CSV file
df = pd.read_csv("orders.csv")

# 1. Find missing values
print("Missing values:")
print(df.isna().sum())

# 2. Find duplicate rows
print("\nDuplicate rows:")
print(df.duplicated().sum())

# 3. Remove duplicate rows
df = df.drop_duplicates()

# 4. Convert amount to numeric
df["amount"] = pd.to_numeric(df["amount"], errors="coerce")

# 5. Fill missing amount with median
median_amount = df["amount"].median()
df["amount"] = df["amount"].fillna(median_amount)

print("\nMedian used:", median_amount)

# 6. Convert order_id to string
df["order_id"] = df["order_id"].astype(str)

# 7. Group by customer and aggregate
result = df.groupby("customer_id").agg(
    total=("amount", "sum"),
    orders=("order_id", "count")
)

print("\nCustomer Summary:")
print(result)
