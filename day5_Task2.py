import pandas as pd
import numpy as np

# Change this to the name of your employee dataset.
INPUT_FILE = "employees.csv"
df = pd.read_csv(INPUT_FILE)

print("FIRST 5 ROWS")
print(df.head())
print("\nDataset shape:", df.shape)

# Summary statistics for numeric columns.
numeric_cols = df.select_dtypes(include="number").columns
print("\nSUMMARY STATISTICS")
print(df[numeric_cols].agg(["mean", "median", "min", "max", "std"]).round(2))

# Group comparisons using available categorical columns.
for group_col in ["department", "city", "gender", "contract_type"]:
    if group_col in df.columns:
        print(f"\nGROUP COUNTS: {group_col}")
        print(df[group_col].value_counts(dropna=False))
        if "salary" in df.columns:
            print(f"\nSALARY BY {group_col.upper()}")
            print(df.groupby(group_col, dropna=False)["salary"].agg(
                ["count", "mean", "median", "min", "max"]
            ).round(2))

# Correlation matrix and top 3 distinct numeric relationships.
corr = df[numeric_cols].corr(numeric_only=True)
print("\nCORRELATION MATRIX")
print(corr.round(3))

if len(numeric_cols) >= 2:
    upper = corr.where(np.triu(np.ones(corr.shape), k=1).astype(bool))
    pairs = upper.stack().reset_index()
    pairs.columns = ["Column 1", "Column 2", "Correlation"]
    pairs["Absolute correlation"] = pairs["Correlation"].abs()
    print("\nTOP 3 CORRELATION RELATIONSHIPS")
    print(pairs.sort_values("Absolute correlation", ascending=False)
          .head(3).drop(columns="Absolute correlation").round(3).to_string(index=False))
else:
    print("Not enough numeric columns to calculate relationships.")

# Five numeric business questions (when matching columns exist).
print("\nBUSINESS QUESTIONS")
if "salary" in df.columns:
    print(f"1. Average salary: {df['salary'].mean():.2f}")
    print(f"2. Highest salary: {df['salary'].max()}")
    print(f"3. Lowest salary: {df['salary'].min()}")
else:
    print("1-3. Salary questions skipped: no 'salary' column found.")

if "department" in df.columns and "salary" in df.columns:
    avg_salary = df.groupby("department")["salary"].mean()
    if not avg_salary.empty:
        print(f"4. Highest-paying department: {avg_salary.idxmax()} "
              f"(average salary: {avg_salary.max():.2f})")
    print("5. Employee count by department:")
    print(df["department"].value_counts().to_string())
elif "department" in df.columns:
    print("Department counts:")
    print(df["department"].value_counts().to_string())
else:
    print("Department questions skipped: no 'department' column found.")

# Merge with a small example department-budget table.
if "department" in df.columns:
    departments = df["department"].dropna().unique()
    budget = pd.DataFrame({
        "department": departments,
        "budget": [(i + 1) * 100000 for i in range(len(departments))]
    })
    merged = pd.merge(df, budget, on="department", how="left")
    merged.to_csv("employees_merged.csv", index=False)
    print("\nMERGED TABLE (first 5 rows)")
    print(merged.head())
    print("Saved: employees_merged.csv")
    print("Note: budget values are example values for demonstrating pd.merge.")

    # Bonus pivot table using two categorical columns, where possible.
    category_candidates = [
        c for c in ["gender", "city", "contract_type"] if c in df.columns
    ]
    if category_candidates and "salary" in df.columns:
        pivot_col = category_candidates[0]
        pivot = pd.pivot_table(
            df, index="department", columns=pivot_col,
            values="salary", aggfunc="mean"
        )
        print(f"\nBONUS PIVOT: MEAN SALARY BY DEPARTMENT AND {pivot_col.upper()}")
        print(pivot.round(2))
    else:
        print("\nPivot table skipped: needs department, another categorical column, and salary.")

print("\nEDA COMPLETED")
