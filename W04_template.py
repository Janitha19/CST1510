
"""
RECORD CHECK - my version
===========================

Name  : Janitha
Lane  : Cyber
Date  : 10/11/26

Run it: python template.py
"""

# =================================================================== FUNCTIONS

def check_record(value, limit):
    """Calculates the difference, percentage and status."""

    difference = limit - value
    percent = (value / limit) * 100

    if percent >= 100:
        status = "OVER LIMIT"
    else:
        status = "OK"

    return difference, percent, status


def print_report(label, value, limit, difference, percent, status):
    """Prints the report for one record."""

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


def load_records(path):
    """Reads records from a file and returns a list of dictionaries."""

    records = []

    with open(path, "r") as file:
        for line in file:
            label, value, limit = line.strip().split(",")

            record = {
                "label": label,
                "value": float(value),
                "limit": float(limit)
            }

            records.append(record)

    return records


# ====================================================================== STORE

records = load_records("records.txt")


# =============================================================== PROCESS + OUTPUT

for record in records:

    label = record["label"]
    value = record["value"]
    limit = record["limit"]

    difference, percent, status = check_record(value, limit)

    print_report(label, value, limit, difference, percent, status)


# ==========================================================================

