
"""
RECORD CHECK - my version
===========================

Name  : Janitha
Lane  : Cyber
Date  : 10/11/26
"""

import pandas as pd
from io import StringIO

# CSV data
csv_data = """label,value,limit
10.0.0.5,12,400
10.0.0.6,45,500
10.0.0.7,110,100
"""

# Read CSV data
df = pd.read_csv(StringIO(csv_data))

# Calculate percentage
df["percent"] = (df["value"] / df["limit"]) * 100

# Calculate status
df["status"] = "OK"
df.loc[df["percent"] >= 100, "status"] = "OVER LIMIT"
df.loc[(df["percent"] >= 90) & (df["percent"] < 100), "status"] = "WARNING"

# Display results
print(df)
