# Very simple Apriori-style program.
# No itertools or external libraries are used.

transactions = [
    ["milk", "bread", "eggs"],
    ["milk", "bread"],
    ["milk", "eggs"],
    ["bread", "eggs"],
    ["milk", "bread", "eggs"]
]

minimum_support = 3

items = ["bread", "eggs", "milk"]

print("Frequent 1-itemsets")

frequent = []

for item in items:
    count = 0

    for transaction in transactions:
        if item in transaction:
            count = count + 1

    if count >= minimum_support:
        frequent.append([item])
        print(item, "count =", count)

print("\nFrequent 2-itemsets")

for i in range(len(items)):
    for j in range(i + 1, len(items)):
        first = items[i]
        second = items[j]
        count = 0

        for transaction in transactions:
            if first in transaction and second in transaction:
                count = count + 1

        if count >= minimum_support:
            print(first, "+", second, "count =", count)