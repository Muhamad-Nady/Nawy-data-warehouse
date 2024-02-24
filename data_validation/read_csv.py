import pandas as pd
df = pd.read_csv("/home/nady/Desktop/nawy_project/home_compound.csv")
duplicates_mask = df.duplicated(subset=["id"])
duplicate_rows = df[duplicates_mask]
print(duplicate_rows)
print(df.head())