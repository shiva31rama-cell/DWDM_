# Simple association-rule demonstration.
# Rule: milk -> bread
# No association-rule library is used.

transactions = [
    ["milk", "bread", "eggs"],
    ["milk", "bread"],
    ["milk", "eggs"],
    ["bread", "eggs"],
    ["milk", "bread", "eggs"]
]

milk_count = 0
bread_count = 0
both_count = 0

for transaction in transactions:
    has_milk = "milk" in transaction
    has_bread = "bread" in transaction

    if has_milk:
        milk_count += 1
    if has_bread:
        bread_count += 1
    if has_milk and has_bread:
        both_count += 1

support = both_count / len(transactions)
confidence = both_count / milk_count

print("Rule: milk -> bread")
print("Support =", support)
print("Confidence =", confidence)

if confidence >= 0.70:
    print("Strong rule")
else:
    print("Weak rule")