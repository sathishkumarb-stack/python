
import pandas as pd
import numpy as np

# 1. Load dataset
df = pd.read_csv("employees.csv")

# Before cleaning summary
before_rows = len(df)
before_missing = int(df.isnull().sum().sum())
before_duplicates = int(df.duplicated().sum())

print("BEFORE CLEANING")
print("Rows:", before_rows)
print("Missing values:", before_missing)
print("Duplicates:", before_duplicates)

# 2. Remove duplicate rows
df = df.drop_duplicates().copy()

# 3. Standardize column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# 4. Clean text and fix data types
for col in df.columns:

    if df[col].dtype == "object":
        # Remove unwanted spaces
        df[col] = df[col].apply(
            lambda x: x.strip() if isinstance(x, str) else x
        )

        # Convert empty strings to missing values
        df[col] = df[col].replace("", np.nan)

        # Convert date columns
        if "date" in col or "time" in col:
            converted = pd.to_datetime(
                df[col], errors="coerce"
            )
            if converted.notna().sum() > 0:
                df[col] = converted
                continue

        # Convert numeric values stored as text
        if "id" not in col:
            numeric = pd.to_numeric(
                df[col].astype(str).str.replace(",", ""),
                errors="coerce"
            )
            valid = df[col].notna().sum()

            if valid > 0 and numeric.notna().sum() / valid >= 0.8:
                df[col] = numeric
                continue

        # Standardize categorical text
        if df[col].dtype == "object":
            df[col] = df[col].apply(
                lambda x: x.title() if isinstance(x, str) else x
            )

# 5. Handle missing values
missing_decisions = {}

for col in df.columns:
    missing_count = int(df[col].isnull().sum())

    if missing_count == 0:
        missing_decisions[col] = "No missing values"
        continue

    if pd.api.types.is_numeric_dtype(df[col]):
        median = df[col].median()

        if pd.notna(median):
            df[col] = df[col].fillna(median)
            missing_decisions[col] = (
                f"Filled {missing_count} missing values with median"
            )
        else:
            df[col] = df[col].fillna(0)
            missing_decisions[col] = (
                "Filled with 0 because median was unavailable"
            )
    else:
        mode = df[col].mode(dropna=True)

        if not mode.empty:
            df[col] = df[col].fillna(mode.iloc[0])
            missing_decisions[col] = (
                f"Filled {missing_count} missing values with mode"
            )
        else:
            df[col] = df[col].fillna("Unknown")
            missing_decisions[col] = (
                "Filled with Unknown because no mode was available"
            )

# 6. Detect outliers using IQR rule
outlier_report = {}

numeric_cols = df.select_dtypes(include="number").columns

for col in numeric_cols:
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1

    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr

    outliers = (df[col] < lower) | (df[col] > upper)
    outlier_report[col] = int(outliers.sum())

    # Keep outliers unchanged; flag them for review.
    # Extreme values may be valid observations.

# 7. Create before/after summary
summary = pd.DataFrame({
    "Metric": ["Rows", "Missing Values", "Duplicates"],
    "Before": [
        before_rows,
        before_missing,
        before_duplicates
    ],
    "After": [
        len(df),
        int(df.isnull().sum().sum()),
        int(df.duplicated().sum())
    ]
})

print("\nBEFORE / AFTER SUMMARY")
print(summary.to_string(index=False))

print("\nMISSING VALUE DECISIONS")
for col, reason in missing_decisions.items():
    print(f"{col}: {reason}")

print("\nIQR OUTLIER COUNTS")
for col, count in outlier_report.items():
    print(f"{col}: {count} outliers (flagged for review)")

# 8. Save cleaned dataset and reports
df.to_csv("clean_data.csv", index=False)
summary.to_csv("cleaning_summary.csv", index=False)

print("\nCleaned data saved as clean_data.csv")
print("Summary saved as cleaning_summary.csv")
