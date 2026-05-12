
# PANDAS BASICS 


# Analogy
#   Think of pandas as a very smart SPREADSHEET ENGINE inside Python
#   - A DataFrame   = an entire Excel sheet (rows x collumns)
#   - A Series      = a single column in that sheet
#   - An Index      = the row numbers on the left side of the sheet


# Why pandas matters for ML: every sklearn model, every feature-eingineering step,
# every drift-detection (PSI, KS) you build in P2 starts with a
# DataFrame. Knowing pandas deeply = faster iteration on everything downstream.



import pandas as pd
import numpy as np

print("=" * 60)
print("     PANDAS BASICS - COMPLETE WALKTHROUGH")
print("=" * 80)


# 1. Creating DATA STRUCTURES


# Think of it like filling ina blank Excel file from scratch.

print("\n--- CREATING SERIES & DATAFRAMES ---\n")

# Series - a single named column
# Analogy: one column ripped out of a spreadsheet, with its row labels intact
ages = pd.Series([25, 30, 22, 35], index=["Alice", "Bob", "Carol", "Dave"])
print("Series (ages):\n", ages)
print("dtype:", ages.dtype)     # pandas infers types automatically

#------- DataFrame from a dict: the most common way to create one ----
# Analogy: each dict key is a column header: each list is the column's data

data = {
    "name":         ["Alice", "Bob", "Carol", "Dave", "Eve"],
    "age":          [25,       30,    22,      35,      28 ],
    "salary":       [50000,    80000, 45000,   90000,   60000],
    "department":   ["HR",     "Eng", "HR",    "Eng",   "Mrkt"],
    "active":       [True,      True,   False,  True,    False],
}
df = pd.DataFrame(data)
print("\nDataFrame:\n", df)


# ---- DataFrame from CSV (the real-workd way)------
# df = pandas.read_csv("your_file.csv")   

# FIRST LOOK AT YOUR DATA

# Analogy: you open a new EXCEL file - first thing you do is scroll around
# to understand its shape and smell.


print("\n-----FIRST LOOK\n")


print("Shape (rows, cols):", df.shape)          # how big is the table ?
print("\nColumn names:", df.columns.tolist())
print("\nData types:\n", df.dtypes)             
print("\nFirst 3 rows:\n", df.head(3))
print("\nLast 2 rows:\n", df.tail(2))
print("\nQuick stats:\n", df.describe())        # count/mean/std/min/quartiles
print("\nMissing values\n", df.isnull().sum())  # NaN count per column


# SELECTING DATA - INDEXING & SLICING

# Analogy: in Excel you click a cell, a column or drag a range
# In pandas you have two tools: .loc (label-based) and .iloc (position-based)

print("\n--------- SELECTING DATA -------\n")

# Select a single column -> returns a Series
print("Single column (salary):\n", df["salary"])

# Select multiple columns -> returns a DataFrame
print("\nTwo columns:\n", df[["name", "salary"]])

# .loc - uses LABELS (column names, index labels)
# Analogy: "give me row labelled 2, column labelled 'age"
print("\n.loc row 2:\n", df.loc[2])
print("\n.loc rows 0-2, specific cols:\n", df.loc[0:2, ["name", "salary"]])

# .iloc - use INTEGER POSITIONS (0-based, like Python lists)
# Analogy: "give me the 1st row, 3rd column"  (counting from 0)
print("\n.iloc first row\n", df.iloc[0])
print("\n.iloc rows 0-2, cols 0-2:\n", df.iloc[0:3, 0:3])


# Boolean indexing - filter rows by a condition
# Analogy: Excel's "Filter" button, but written as code
high_earners = df[df["salary"] > 55000]
print("\nHigh earners (salary > 55k): \n", high_earners)

# Combine conditions with & (and) | (or) - MUST use parentheses!
eng_high = df[(df["department"] == "Eng") & (df["salary"] >  70000)]
print("\nEng + salary > 70k:\n", eng_high)


# ADDING, MODIFYING, DROPPING COLUMNS

# Analogy: inserting/deleting columns in Excel, but tracked in code


print("\n-------- MODIFYING COLUMNS ---------\n")

# Add a new column (derived from existing ones)
df["salary_monthly"] = df["salary"] / 12
print("Added monthly salary:\n", df[["name", "salary", "salary_monthly"]])

# Modify an existing column - apply a function to every row
# .apply() is like a dragging a formula down Excel column

df["name_upper"] = df["name"].apply(lambda x: x.upper())
print("\nUpper-cased names:\n", df["name_upper"])

# Drop columns (axis=1 = columns; axis=0 = rows)
df_clean = df.drop(columns=["name_upper", "salary_monthly"])
print("\nAfter dropping temp columns:\n", df_clean.columns.to_list())



# HANDLING MISSING DATA

# Analogy: blank cells in Excel. Pandas represents them as NaN (Not a Number).
# In ML, NaN values break most algorithms - always handle them

print("\n------MISSING DATA----------\n")


# Inject some NaN values to practice with
df_with_nulls = df_clean.copy()
df_with_nulls.loc[1, "salary"] = np.nan
df_with_nulls.loc[3, "age"] = np.nan
print("DataFrame with NaNs:\n", df_with_nulls)


# Detect missing values
print("\nIs null?\n", df_with_nulls.isnull())
print("\nNull count per col:\n", df_with_nulls.isnull().sum())

# Drop rows that have ANY missing value
print("\nDrop rows with NaN:\n", df_with_nulls.dropna())

# Fill NaN with a fixed value
print("\nFill NaN salary with 0:\n",
      df_with_nulls["salary"].fillna(0))

# Fill NaN with the column mean (common in ML preprocessing)
mean_salary = df_with_nulls["salary"].mean()
df_with_nulls["salary"] = df_with_nulls["salary"].fillna(mean_salary)
print("\nAfter filling salary NaN with mean:\n", df_with_nulls["salary"])

# SORTING & RANKING 

# Analogy: clicking the column header in Excel to sort ascendting/descending

print("\n----- SORTING -----\n")

# Sort by a single column
print("Sorted by salary (desc):\n",
      df_clean.sort_values("salary", ascending=False))


# Sort multiple columns - department asc, then salary desc within each dept
print("\nSorted by dept then salary:\n",
      df_clean.sort_values(["department", "salary"], ascending=[True, False]))



# GROUPBY - SPLIT -> APPLY -> COMBINE

# This is one of pandas' most powerful tools.
# Analogy: Excel PivotTable. Group rows by category, compute stats per group


# Mental model: GroupBy works in 3 steps:
#   1. SPLIT    - divide the DataFrame into groups (e.g, by department)
#   2. APPLY    - compute something on each group (mean, sum, count, custom fn)
#   3. COMBINE  - stitch results back into a new DataFrame


print("\n------- GROUPBY ------\n")


# Average salary per department
avg_salary = df_clean.groupby("department")["salary"].mean()
print("Avg salary by department:\n", avg_salary)

# Multiple aggregations at once
agg = df_clean.groupby("department").agg(
    headcount=("name", "count"),
    avg_salary=("salary", "mean"),
    max_age=("age", max),
)
print("\nGroupBy multi-agg:\n", agg)

# GroupBy + filter:  only groups with more than 1 person
big_depts = df_clean.groupby("department").filter(lambda g: len(g) > 1)
print("\nDepts with >1 person:\n", big_depts)

