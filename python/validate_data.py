import pandas as pd

# df = pd.read_csv("data/output.csv")
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

df = pd.read_csv(DATA_DIR / "output.csv")

print("=" * 40)
print("DATA VALIDATION REPORT")
print("=" * 40)

print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")

print("\nMissing Values")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())

print("\nValidation Complete")