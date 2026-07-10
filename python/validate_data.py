import pandas as pd

df = pd.read_csv("../data/output.csv")

print("Rows:", len(df))
print("Missing values:")
print(df.isnull().sum())
