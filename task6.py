
import pandas as pd

# Create orders.csv
orders_data = {
    "order_id": ["1", "2", "3", "4", "5"],
    "customer_id": [101, 102, 101, 103, 104],
    "amount": [500, 600, 700, 300, 900]
}

orders = pd.DataFrame(orders_data)
orders = orders.drop_duplicates()

orders.to_csv("orders.csv", index=False)

# Create customers.csv
customers_data = {
    "customer_id": [101, 102, 103, 105],
    "name": ["Arun", "Priya", "Rahul", "Divya"],
    "city": ["Chennai", "Mumbai", "Chennai", "Bangalore"]
}

customers = pd.DataFrame(customers_data)
customers.to_csv("customers.csv", index=False)

# Load both CSV files
orders = pd.read_csv("orders.csv")
customers = pd.read_csv("customers.csv")

# 1. Inner join
inner = pd.merge(
    orders, customers,
    on="customer_id",
    how="inner"
)

print("Inner join rows:", len(inner))
print(inner)

# 2. Left join: customers with no orders
left = pd.merge(
    customers, orders,
    on="customer_id",
    how="left",
    indicator=True
)

no_orders = left[left["_merge"] == "left_only"]

print("\nCustomers with no orders:")
print(no_orders[["customer_id", "name", "city"]])

# 3. Outer join: find orders without a customer record
outer = pd.merge(
    orders, customers,
    on="customer_id",
    how="outer",
    indicator=True
)

no_customer = outer[outer["_merge"] == "left_only"]

print("\nOrders without customer records:")
print(no_customer[["order_id", "customer_id", "amount"]])
