# Create unique simulated records using basic Python.
# A record is unique when age and score are not repeated together.

records = []

for age in range(18, 28):
    score = 50 + (age - 18) * 3
    record = [age, score]
    records.append(record)

print("Unique simulated dataset")
for record in records:
    print(record)

print("Total records =", len(records))