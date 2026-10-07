# 1. Create an empty dataset
records = []

# 2. Generate unique records
for age in range(18, 28):
    score = 50 + (age - 18) * 3
    records.append([age, score])

# 3. Display the dataset
print("--- SIMULATED DATASET ---")

for record in records:
    print("Age =", record[0], "Score =", record[1])

# 4. Display total records
print("Total unique records =", len(records))
