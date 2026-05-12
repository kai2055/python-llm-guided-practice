
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