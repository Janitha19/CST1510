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


# ==================================================================== INPUT

# 1. Ask the user for three values.

label = input("Enter source IP: ")
first = float(input("Enter failed logins: "))
second = float(input("Enter total attempts: "))


# ================================================================== PROCESS

# 2. Work out the difference and percentage.

difference = second - first
percent = (first / second) * 100


# =================================================================== OUTPUT

# 3. Print the report.

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print(f"  Failed logins : {first:g}")
print(f"  Total attempts: {second:g}")

print("=" * 34)


# ==========================================================================

# 4. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and write the error in your journal
#    [ ] Check every variable name says what it holds
#    [ ] Show it to the person next to you
