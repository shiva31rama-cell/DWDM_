# 1. Create a small sample dataset
data = [
    ["Sunny", 30, "Yes"],
    ["Rainy", 20, "No"],
    ["Cloudy", 25, "Yes"],
    ["Sunny", 32, "Yes"],
    ["Rainy", 18, "No"]
]

print("--- DATASET ---")
for row in data:
    print(row)

# 2. Display the number of records
print("\nTotal records =", len(data))

# 3. Display attribute names and types
print("\n--- ATTRIBUTES ---")
print("Weather -> Nominal")
print("Temperature -> Numeric")
print("Play -> Class attribute")

# 4. Count the class values
yes_count = 0
no_count = 0

for row in data:
    if row[2] == "Yes":
        yes_count = yes_count + 1
    else:
        no_count = no_count + 1

print("\nClass count")
print("Yes =", yes_count)
print("No  =", no_count)

# 5. Observation
print("\nObservation: The dataset contains", len(data), "records.")
print("The class values are Yes and No.")
