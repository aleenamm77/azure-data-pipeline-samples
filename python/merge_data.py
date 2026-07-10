import json
import pandas as pd
from logger import logger

logger.info("Loading customer data...")


with open("data/customers.json") as f:
    customers = json.load(f)
logger.info("Loading order data...")

with open("data/orders.json") as f:
    orders = json.load(f)
logger.info("Merging datasets...")

customers_df = pd.DataFrame(customers)
orders_df = pd.DataFrame(orders)

merged = orders_df.merge(customers_df, on="customer_id")
logger.info("Saving output.csv")

merged.to_csv("data/output.csv", index=False)
logger.info("ETL completed successfully.")
print(merged)
