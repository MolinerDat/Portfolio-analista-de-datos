 1. Import & Read Your CSV

import pandas as pd

# Replace with your real file name or path
df = pd.read_csv("your_file.csv")

# Show first 5 rows
df.head()

 2. Clean Column Names (Optional but recommended)

# Lowercase and replace spaces with underscores
df.columns = df.columns.str.lower().str.replace(" ", "_")

3. Drop Columns You Don’t Need

# Drop columns by name
columns_to_drop = ["timestamp", "email", "ip_address"]
df = df.drop(columns=columns_to_drop, errors="ignore")

4. Remove or Handle Missing Values

# Option A: Drop rows with missing data in key columns
df = df.dropna(subset=["satisfaction", "age"])

# Option B: Fill missing data (e.g. fill with mean)
df["income"] = df["income"].fillna(df["income"].mean())

5. Basic Summary

print(df.info())       # Structure and types
print(df.describe())   # Numeric summary
print(df["city"].value_counts())  # Frequency count

6. Export Clean Data (Optional)

df.to_csv("my_exports/cleaned_data.csv", index=False)
print("✅ Clean data saved.")
