"""
RECORD CHECK  -  my version
===========================

Name  :Janitha
Lane  :Cyber
Date  :10/11/26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ====================================================================== CLASS
# 1. Define a class called Record.
#    Threshold : __init__(self, label, value, limit) storing all three as attributes. No methods yet.

class Record:
    def __init__(self, label, value, limit):
        self.label = label
        self.value = float(value)
        self.limit = float(limit)


# ==================================================================== RECORDS
# 2. Create your records.
#    Threshold : create at least 2 Record instances directly in the code.

records = [
    Record("srv-01", 87, 120),
    Record("srv-02", 110, 100)
]


# ==================================================================== OUTPUT
# 3. Print a report for each record.
#    Threshold : label, value, limit, inside a border.

for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)
    print(f"Used    : {record.value:6.2f}")
    print(f"Total   : {record.limit:6.2f}")
    print("=" * 34)


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers by hand
#    [ ] Check every method only reads/changes its OWN object (self) -
#        nothing reaches outside itself
#    [ ] Check every method and __init__ has a one-line docstring
