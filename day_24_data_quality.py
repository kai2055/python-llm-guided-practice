"""
Data Quality in CSV Files

What is data quality?
---------------------
Data quality refers to the fitness of data for its intended use. High-quality
data is:
- Accurate: Correctly represents reality
- Complete: No missing critical information
- Consistent: Follows the same format and rules throughout
- Valid: Conforms to expected formats, ranges, and business rules
- Unique: No unintended duplicates


Why data quality matters?
------------------------
1. INCORRECT ANALYSIS
    - Missing values can skew averages and statistics
    - Wrong data types prevent mathematical operation
    - Duplicates inflate counts and distort patterns

2. BROKEN PIPELINES
    - Unexpected formats crash automated systems
    - Type mismatches cause processing failures
    - Invalid values trigger exceptions in production

3. MISLEADING RESULTS
    - Bad data leads to bad decisions
    - Models trained on poor data make poor predictions
    - Reports based on dirty data misinform stakeholders

    
THE GOLDEN RULE:
------------------
Always validate and clean data BEFORE analysis or modeling.
Data quality checks should be the FIRST step in any data pipeline.


DETECTION vs. FIXING
--------------------
- DETECTION: Finding problems in data (what this program focuses on)
- FIXING: Correcting ot handling those problems (requires domain knowledge)


This program teaches you to DETECT issues. Fixing requires understanding:
- Business context (what values make sense?)
- Downstream use (how will this data be used?)
- Stakeholders requirements (what's acceptable)

Let's explore common data quality issues in CSV files..

"""

import pandas as pd
import numpy as np

# Part 1: Creating a sample dataset with intentional quality issues
