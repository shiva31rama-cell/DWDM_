# 1. Create transaction data
transactions = [
    ["Milk", "Bread", "Eggs"],
    ["Milk", "Bread"],
    ["Milk", "Eggs"],
    ["Bread", "Eggs"],
    ["Milk", "Bread", "Eggs"]
]

# Rule: Milk -> Bread
milk_count = 0
bread_count = 0
both_count = 0

# 2. Count occurrences
for transaction in transactions:
    has_milk = "Milk" in transaction
    has_bread = "Bread" in transaction

    if has_milk:
        milk_count = milk_count + 1

    if has_bread:
        bread_count = bread_count + 1

    if has_milk and has_bread:
        both_count = both_count + 1

# 3. Calculate support and confidence
support = both_count / len(transactions)
confidence = both_count / milk_count

print("--- ASSOCIATION RULE ---")
print("Rule: Milk -> Bread")
print("Support =", support)
print("Confidence =", confidence)

# 4. Observation
if confidence >= 0.70:
    print("Observation: Strong rule")
else:
    print("Observation: Weak rule")
