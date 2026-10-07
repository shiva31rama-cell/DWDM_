# EXPERIMENT 09 - FREQUENT ITEMSETS
# No external package is needed.
# Dataset = shopping transactions.
# An itemset is frequent when support count >= minimum support.

transactions = [
    ["A", "B", "C"],
    ["A", "B"],
    ["A", "C"],
    ["B", "C"],
    ["A", "B", "C"]
]

minimum_support = 3
items = ["A", "B", "C"]

print("FREQUENT 1-ITEMSETS")

frequent_items = []

for item in items:
    count = 0

    for transaction in transactions:
        if item in transaction:
            count = count + 1

    if count >= minimum_support:
        frequent_items.append(item)
        print(item, "support =", count)

print("\nFREQUENT 2-ITEMSETS")

for i in range(len(frequent_items)):
    for j in range(i + 1, len(frequent_items)):
        item1 = frequent_items[i]
        item2 = frequent_items[j]
        count = 0

        for transaction in transactions:
            if item1 in transaction and item2 in transaction:
                count = count + 1

        if count >= minimum_support:
            print(item1, item2, "support =", count)

print("\nRESULT: Frequent itemsets found.")
