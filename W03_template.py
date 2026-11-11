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


# =================================================================== FUNCTIONS

def status_of(percent):
    """Returns the status based on the percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


def check(value, limit):
    """Calculates and returns the difference and percentage."""
    difference = limit - value
    percent = (value / limit) * 100
    return difference, percent


def print_report(label, value, limit, difference, percent, status):
    """Prints the complete record check report."""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)

    print(f"  Used       : {value:10.2f}")
    print(f"  Total      : {limit:10.2f}")
    print(f"  Free       : {difference:10.2f}")
    print(f"  Percent    : {percent:10.2f} %")
    print(f"  Status     : {status:>10}")

    print("=" * 34)


# ==================================================================== INPUT

over_limit_count = 0

while True:

    label = input("Enter hostname (or quit to stop): ")

    if label.lower() == "quit":
        break

    value = float(input("Enter GB used: "))
    limit = float(input("Enter GB total: "))


    # ================================================================== PROCESS

    difference, percent = check(value, limit)

    status = status_of(percent)

    if status == "OVER LIMIT":
        over_limit_count += 1


    # =================================================================== OUTPUT

    print_report(label, value, limit, difference, percent, status)


# Print the final session count after the loop

print()
print("=" * 34)
print(f"OVER LIMIT records: {over_limit_count}")
print("=" * 34)

# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every function does one job - if a function both calculates
#        and prints, split it
