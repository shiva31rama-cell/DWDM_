# Simple Apriori-style demonstration.
# Only lists, loops and if statements are used.

transactions = [
    ["milk", "bread", "eggs"],
    ["milk", "bread"],
    ["milk", "eggs"],
    ["bread", "eggs"],
    ["milk", "bread", "eggs"]
]

items = ["bread", "eggs", "milk"]
minimum_support_count = 3

print("Frequent 1-itemsets")

for i in range(len(items)):
    count = 0

    for transaction in transactions:
        for item in transaction:
            if item == items[i]:
                count += 1
                break

    if count >= minimum_support_count:
        print(items[i], "count =", count)

print("\nFrequent 2-itemsets")

for i in range(len(items)):
    for j in range(i + 1, len(items)):
        count = 0

        for transaction in transactions:
            found_first = False
            found_second = False

            for item in transaction:
                if item == items[i]:
                    found_first = True
                if item == items[j]:
                    found_second = True

            if found_first and found_second:
                count += 1

        if count >= minimum_support_count:
            print(items[i], "+", items[j], "count =", count)