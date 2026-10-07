# 1. Create a simple sales data cube
sales = [
    ["Laptop", "Bhimavaram", "January", 50000],
    ["Laptop", "Bhimavaram", "February", 60000],
    ["Phone", "Bhimavaram", "January", 30000],
    ["Phone", "Vijayawada", "January", 40000]
]

print("--- ORIGINAL DATA ---")
for row in sales:
    print(row)

# 2. SLICE
# Select one value from one dimension.
print("\n--- SLICE: Product = Laptop ---")
for row in sales:
    if row[0] == "Laptop":
        print(row)

# 3. DICE
# Select records using two conditions.
print("\n--- DICE: Phone and Bhimavaram ---")
for row in sales:
    if row[0] == "Phone" and row[1] == "Bhimavaram":
        print(row)

# 4. ROLL-UP
# Move from detailed data to summary data.
laptop_total = 0
phone_total = 0

for row in sales:
    if row[0] == "Laptop":
        laptop_total = laptop_total + row[3]
    else:
        phone_total = phone_total + row[3]

print("\n--- ROLL-UP: Total by Product ---")
print("Laptop =", laptop_total)
print("Phone  =", phone_total)

# 5. DRILL-DOWN
# Show detailed records from the summary level.
print("\n--- DRILL-DOWN: Detailed Sales ---")
for row in sales:
    print("Product:", row[0], "City:", row[1],
          "Month:", row[2], "Amount:", row[3])

# 6. PIVOT
# Change the arrangement of dimensions.
print("\n--- PIVOT ---")
print("Product       January    February")
print("Laptop        50000      60000")
print("Phone         70000      0")
