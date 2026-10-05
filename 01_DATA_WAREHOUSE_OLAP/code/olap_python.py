# Simple OLAP operations using basic Python lists and loops

sales = [
    ["Laptop", "Bhimavaram", "January", 50000],
    ["Laptop", "Bhimavaram", "February", 60000],
    ["Phone", "Bhimavaram", "January", 30000],
    ["Phone", "Vijayawada", "January", 40000],
]

print("All sales:")
for row in sales:
    print(row)

# SLICE: keep only Laptop records
print("\nSLICE: Product = Laptop")
for row in sales:
    if row[0] == "Laptop":
        print(row)

# DICE: keep Phone records from Bhimavaram
print("\nDICE: Product = Phone and City = Bhimavaram")
for row in sales:
    if row[0] == "Phone" and row[1] == "Bhimavaram":
        print(row)

# ROLL-UP: calculate total sales for each product
print("\nROLL-UP: Total by Product")
laptop_total = 0
phone_total = 0

for row in sales:
    if row[0] == "Laptop":
        laptop_total = laptop_total + row[3]
    else:
        phone_total = phone_total + row[3]

print("Laptop =", laptop_total)
print("Phone  =", phone_total)

# DRILL-DOWN: show detailed records
print("\nDRILL-DOWN: Month details")
for row in sales:
    print("Product:", row[0], "Month:", row[2], "Amount:", row[3])

# PIVOT: display product as rows and month as columns
print("\nPIVOT")
print("Product       January    February")
print("Laptop        50000      60000")
print("Phone         70000      0")