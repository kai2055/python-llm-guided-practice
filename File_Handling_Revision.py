
"""
Fundamentals Revision: File Handling, JSON, CSV
"""

import json
import csv
import os

# PART 1: BASIC FILE HANDLING



# Writing to a file (mode "W" ERASES existing content)
with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("First line of notes.\n")
    f.write("Second line.\n")
# File is auto-closed here when the 'with' block ends.


# Appending (mode "a" keeps existing content, adds to end)
with open("notes.txt", "a", encoding="utf-8") as f:
    f.write("Third line, added later.\n")

# Reading: three common ways 
with open("notes.txt", "r", encoding="utf-8") as f:
    whole_text = f.read()    # entire file as one string
print("read( output:)")
print(whole_text)

with open("notes.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()      # list of lines (keeps \n characters)
print("readlines() output:", lines)


with open("notes.txt", "r", encoding="utf-8") as f:
    for line in f:      # iterate line-by-line  (memory efficient)
        print("line:", line.strip())    # strip() removes the trailing \n

# Checking if a file exists before opening it 
if os.path.exists("notes.txt"):
    print("notes.txt exists")


# PART 2: JSON
# Flattens Python data into text that any language/system can read back
# dump/load = work with files. dumps/loads = work with strings


user_data = {
    "name": "Flyin Monk",
    "city": "Berlin",
    "skills": ["Python", "ML", "Docker"],
    "active": True,
    "projects_done": 2,
}

# Writing JSON to a file
with open("user.json", "w", encoding="utf-8") as f:
    json.dump(user_data, f, indent=2)   # indent=2 makes it human-readable

# Reading JSON from a file
with open("user.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)
print("Loaded JSON:", loaded)
print("Name field", loaded["name"])     # back to a real Python dict


# JSON as a string (no file involved)
as_string = json.dumps(user_data)       # Python dict -> JSON string
back_to_dict = json.loads(as_string)    # JSON string -> Python dict
print("Round triip OK", back_to_dict == user_data)



# PART 3: CSV

# Rows = lines, columns seperated by commas. Everything becomes a string
# IMPORTANT: always pass newline="" when opening csv files,
# otherwise you can get blank lines on Windows


# Writing CSV with a plain writer (list of lists)

rows = [
    ["name", "city", "projects"],   # header row
    ["Flyin Monk", "Berlin", 2],
    ["Alice", "Munich", 5]

]


with open("people.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(rows)      # writerow() for one, writerows() for many


# Reading CSV with a plain reader
with open("people.csv", "r", newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:      # each row is a list of strings
        print("row:", row)


# DictWriter / DictReader: treat rows as dictionaries 
# This is usually cleaner because you can access columns by name, not index

records = [
    {"name": "Flyin Monk", "city": "Berlin", "projects":2},
    {"name": "Alice", "city": "Munich", "projects": 5},
]

with open("people_dict.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "city", "projects"])
    writer.writeheader()        # writes the column names roe
    writer.writerows(records)

with open("people_dict.csv", "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:      # each row is a dict
        # CSV values come back as strings - convert if needed
        print(f"{row['name']} has {int(row['projects'])} projects")



# PART 4: ERROR HANDLING pattern
# Files might not exist, JSON might be malformed. WRAP risky reads


try:
    with open("does_not_exist.txt", "r", encoding="utf-8") as f:
        content = f.read()
except FileNotFoundError:
    print("File not found - handled gracefully.")
except json.JSONDecodeError as e:
    print(f"Malformed JSON: {e}")