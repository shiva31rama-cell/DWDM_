# EXPERIMENT 06 - ASSOCIATION RULE MINING
# No external package is needed.
# Dataset = shopping transactions.
#
# confidence(A -> B) = support(A and B) / support(A)

transactions = [
    ["Bread", "Milk"],
    ["Bread", "Milk", "Eggs"],
    ["Milk", "Eggs"],
    ["Bread", "Eggs"],
    ["Bread", "Milk", "Eggs"]
]

minimum_support_count = 2
minimum_confidence = 0.60
items = ["Bread", "Milk", "Eggs"]

# Count each single item.
single_count = {}

for item in items:
    single_count[item] = 0

    for transaction in transactions:
        if item in transaction:
            single_count[item] = single_count[item] + 1

# Find rules for every pair.
for i in range(len(items)):
    for j in range(i + 1, len(items)):
        a = items[i]
        b = items[j]
        pair_count = 0

        for transaction in transactions:
            if a in transaction and b in transaction:
                pair_count = pair_count + 1

        if pair_count >= minimum_support_count:
            confidence_a_b = pair_count / single_count[a]
            confidence_b_a = pair_count / single_count[b]

            print(a, "->", b,
                  "support =", pair_count,
                  "confidence =", round(confidence_a_b, 2))

            print(b, "->", a,
                  "support =", pair_count,
                  "confidence =", round(confidence_b_a, 2))

            if confidence_a_b >= minimum_confidence:
                print("Strong rule:", a, "->", b)

            if confidence_b_a >= minimum_confidence:
                print("Strong rule:", b, "->", a)

print("\nRESULT: Association rules generated.")
