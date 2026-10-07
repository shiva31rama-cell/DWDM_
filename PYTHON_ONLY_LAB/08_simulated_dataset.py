# EXPERIMENT 08 - SIMULATED DATASET WITH UNIQUE INSTANCES
# No external package is needed.
# A loop creates a small simulated dataset.
# Every student ID is different, so the instances are unique.

records = []

for i in range(1, 11):
    student_id = "S" + str(i)
    age = 18 + (i % 3)
    marks = 60 + i

    result = "Pass"
    if marks < 65:
        result = "Fail"

    records.append([student_id, age, marks, result])

print("ID  Age  Marks  Result")
for record in records:
    print(record[0], record[1], record[2], record[3])

unique = True

for i in range(len(records)):
    for j in range(i + 1, len(records)):
        if records[i][0] == records[j][0]:
            unique = False

print("\nAll IDs unique =", unique)
print("\nRESULT: Simulated dataset with unique instances created.")
