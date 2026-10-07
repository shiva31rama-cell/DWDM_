# EXPERIMENT 01 - DATA WAREHOUSE + OLAP OPERATIONS
# No external package is needed.
# Dataset fields: city, product, sales.
# OLAP: Slice, Dice, Roll-up, Drill-down and Pivot.

data = [
    {"city": "Vijayawada", "product": "Phone", "sales": 20000},
    {"city": "Vijayawada", "product": "Laptop", "sales": 50000},
    {"city": "Guntur", "product": "Phone", "sales": 15000},
    {"city": "Guntur", "product": "Laptop", "sales": 45000}
]

print("ORIGINAL DATA")
for row in data:
    print(row)

# SLICE = select one value of a dimension.
print("\nSLICE: Vijayawada")
for row in data:
    if row["city"] == "Vijayawada":
        print(row)

# DICE = select more than one condition.
print("\nDICE: Vijayawada + Phone")
for row in data:
    if row["city"] == "Vijayawada" and row["product"] == "Phone":
        print(row)

# ROLL-UP = combine detailed rows into a summary.
city_total = {}
for row in data:
    city = row["city"]
    if city not in city_total:
        city_total[city] = 0
    city_total[city] = city_total[city] + row["sales"]

print("\nROLL-UP: Total sales by city")
for city in city_total:
    print(city, "=", city_total[city])

# DRILL-DOWN = go from summary back to details.
print("\nDRILL-DOWN: Guntur details")
for row in data:
    if row["city"] == "Guntur":
        print(row)

# PIVOT = change the display arrangement.
print("\nPIVOT TABLE")
print("City        Phone   Laptop")
for city in ["Vijayawada", "Guntur"]:
    phone = 0
    laptop = 0

    for row in data:
        if row["city"] == city and row["product"] == "Phone":
            phone = row["sales"]
        if row["city"] == city and row["product"] == "Laptop":
            laptop = row["sales"]

    print(city, phone, laptop)

print("\nRESULT: Basic OLAP operations completed.")
