from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


SCRIPT_DIR = Path(__file__).resolve().parent
CSV_CANDIDATES = (SCRIPT_DIR / "employees.csv", SCRIPT_DIR.parent / "employees.csv")
CSV_PATH = next((path for path in CSV_CANDIDATES if path.is_file()), None)

if CSV_PATH is None:
    candidates = ", ".join(str(path) for path in CSV_CANDIDATES)
    raise FileNotFoundError(
        f"Could not find employees.csv. Checked: {candidates}. "
        "Run the Day 3 script first to create it."
    )

employees = pd.read_csv(CSV_PATH)
required_columns = {"id", "department", "salary"}
missing_columns = required_columns.difference(employees.columns)
if missing_columns:
    missing = ", ".join(sorted(missing_columns))
    raise ValueError(f"{CSV_PATH} is missing required columns: {missing}")


# Average salary by department
average_salary = employees.groupby("department")["salary"].mean().sort_index()
fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar(average_salary.index, average_salary.values, color="steelblue")
ax.set_title("Average Salary by Department")
ax.set_xlabel("Department")
ax.set_ylabel("Average Salary")
ax.bar_label(bars, fmt="%.0f", padding=3)
fig.tight_layout()
fig.savefig(SCRIPT_DIR / "average_salary_by_department.png", dpi=150)
plt.close(fig)

# Salary distribution
fig, ax = plt.subplots(figsize=(8, 5))
ax.hist(employees["salary"], bins=5, color="cornflowerblue", edgecolor="black")
ax.set_title("Distribution of Employee Salaries")
ax.set_xlabel("Salary")
ax.set_ylabel("Number of Employees")
fig.tight_layout()
fig.savefig(SCRIPT_DIR / "salary_histogram.png", dpi=150)
plt.close(fig)

# Employee ID versus salary, grouped by department
fig, ax = plt.subplots(figsize=(8, 5))
for department, group in employees.groupby("department", sort=True):
    ax.scatter(group["id"], group["salary"], label=department, s=60)
ax.set_title("Employee ID vs Salary by Department")
ax.set_xlabel("Employee ID")
ax.set_ylabel("Salary")
ax.legend(title="Department")
fig.tight_layout()
fig.savefig(SCRIPT_DIR / "employee_id_vs_salary.png", dpi=150)
plt.close(fig)

# Monthly sales from January through June
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [12, 15, 14, 18, 22, 25]
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(months, sales, marker="o")
ax.set_title("Monthly Sales (January to June)")
ax.set_xlabel("Month")
ax.set_ylabel("Sales")
fig.tight_layout()
fig.savefig(SCRIPT_DIR / "monthly_sales.png", dpi=150)
plt.close(fig)

print(f"Loaded employee data from: {CSV_PATH}")
print(f"Saved all four charts to: {SCRIPT_DIR}")
