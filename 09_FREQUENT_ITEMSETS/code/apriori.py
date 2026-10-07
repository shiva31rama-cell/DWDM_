# 1. Create transaction data
transactions = [
    ["Milk", "Bread", "Eggs"],
    ["Milk", "Bread"],
    ["Milk", "Eggs"],
    ["Bread", "Eggs"],
    ["Milk", "Bread", "Eggs"]
]

items = ["Milk", "Bread", "Eggs"]
minimum_support = 3

# 2. Generate frequent 1-itemsets
print("--- FREQUENT 1-ITEMSETS ---")

for i in range(len(items)):
    count = 0

    for transaction in transactions:
        if items[i] in transaction:
            count = count + 1

    if count >= minimum_support:
        print([items[i]], "Support Count =", count)

# 3. Generate frequent 2-itemsets
print("\n--- FREQUENT 2-ITEMSETS ---")

for i in range(len(items)):
    for j in range(i + 1, len(items)):
        count = 0

        for transaction in transactions:
            if items[i] in transaction and items[j] in transaction:
                count = count + 1

        if count >= minimum_support:
            print([items[i], items[j]], "Support Count =", count)
