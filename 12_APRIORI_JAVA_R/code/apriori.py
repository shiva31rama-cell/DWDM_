# Basic Apriori idea in Python.
# We count 1-itemsets and 2-itemsets using loops.

transactions = [
    ["milk", "bread", "eggs"],
    ["milk", "bread"],
    ["milk", "eggs"],
    ["bread", "eggs"],
    ["milk", "bread", "eggs"]
]

items = ["milk", "bread", "eggs"]
minimum_support = 3

print("Frequent itemsets")

for i in range(len(items)):
    count = 0

    for transaction in transactions:
        if items[i] in transaction:
            count += 1

    if count >= minimum_support:
        print([items[i]], "support count =", count)

for i in range(len(items)):
    for j in range(i + 1, len(items)):
        count = 0

        for transaction in transactions:
            if items[i] in transaction and items[j] in transaction:
                count += 1

        if count >= minimum_support:
            print([items[i], items[j]], "support count =", count)