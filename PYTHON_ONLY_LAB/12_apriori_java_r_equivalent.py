# EXPERIMENT 12 - APRIORI
# The original lab asks for Java/R.
# This separate Python file is only an easy practice version.
# No external package is needed.
#
# Dataset:
# T1 = A B C
# T2 = A B
# T3 = A C
# T4 = B C
# T5 = A B C

transactions = [
    ["A", "B", "C"],
    ["A", "B"],
    ["A", "C"],
    ["B", "C"],
    ["A", "B", "C"]
]

minimum_support = 3
items = ["A", "B", "C"]

print("STEP 1: SINGLE ITEMS")

for item in items:
    count = 0

    for transaction in transactions:
        if item in transaction:
            count = count + 1

    print(item, "support =", count)

print("\nSTEP 2: ITEM PAIRS")

for i in range(len(items)):
    for j in range(i + 1, len(items)):
        item1 = items[i]
        item2 = items[j]
        count = 0

        for transaction in transactions:
            if item1 in transaction and item2 in transaction:
                count = count + 1

        if count >= minimum_support:
            print(item1, item2, "is frequent")

print("\nRESULT: Apriori processing completed.")
