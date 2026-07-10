import json
import pandas as pd

with open("../data/customers.json") as f:
    customers = json.load(f)

with open("../data/orders.json") as f:
    orders = json.load(f)

customers_df = pd.DataFrame(customers)
orders_df = pd.DataFrame(orders)

merged = orders_df.merge(customers_df, on="customer_id")

merged.to_csv("../data/output.csv", index=False)

print(merged)
