# EXPERIMENT 03 - APRIORI (WEKA APRIORI PRACTICE)
# No external package is needed.
# Dataset = shopping transactions.
# Support = itemset count / total transactions.

transactions = [
    ["Bread", "Milk"],
    ["Bread", "Milk", "Eggs"],
    ["Milk", "Eggs"],
    ["Bread", "Eggs"]
]

minimum_support = 2
items = ["Bread", "Milk", "Eggs"]

print("TRANSACTIONS")
for transaction in transactions:
    print(transaction)

# STEP 1: Find frequent 1-itemsets.
frequent_one = []

print("\nSTEP 1: SINGLE-ITEM SUPPORT")
for item in items:
    count = 0

    for transaction in transactions:
        if item in transaction:
            count = count + 1

    print(item, "->", count)

    if count >= minimum_support:
        frequent_one.append(item)

print("Frequent 1-itemsets =", frequent_one)

# STEP 2: Find frequent pairs.
frequent_two = []

print("\nSTEP 2: PAIR SUPPORT")
for i in range(len(frequent_one)):
    for j in range(i + 1, len(frequent_one)):
        item1 = frequent_one[i]
        item2 = frequent_one[j]
        count = 0

        for transaction in transactions:
            if item1 in transaction and item2 in transaction:
                count = count + 1

        print(item1, "+", item2, "->", count)

        if count >= minimum_support:
            frequent_two.append([item1, item2])

print("Frequent 2-itemsets =", frequent_two)
print("\nRESULT: Frequent itemsets found using Apriori.")
