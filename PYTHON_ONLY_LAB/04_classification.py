# EXPERIMENT 04 - CLASSIFICATION
# This file gives simple Python practice for K-NN, Naive Bayes and
# the basic ID3 decision-tree idea.
# J48 is WEKA's decision-tree classifier, so use WEKA for full J48 results.
# No external package is needed.
#
# Dataset = [study_hours, attendance, class]

data = [
    [2, 60, "Fail"],
    [3, 70, "Fail"],
    [4, 75, "Pass"],
    [5, 80, "Pass"],
    [6, 90, "Pass"]
]

# ---------------- K-NN ----------------
# Distance used here = difference in hours + difference in attendance.
test_hours = 4
test_attendance = 78

best_distance = 999999
best_class = ""

for row in data:
    distance = abs(row[0] - test_hours) + abs(row[1] - test_attendance)

    if distance < best_distance:
        best_distance = distance
        best_class = row[2]

print("K-NN prediction =", best_class)

# ---------------- NAIVE BAYES IDEA ----------------
pass_count = 0
fail_count = 0

for row in data:
    if row[2] == "Pass":
        pass_count = pass_count + 1
    else:
        fail_count = fail_count + 1

print("\nNAIVE BAYES CLASS COUNTS")
print("Pass =", pass_count)
print("Fail =", fail_count)

# ---------------- ID3 BASIC TREE ----------------
print("\nID3 BASIC TREE")
print("IF attendance < 73 THEN Fail")
print("ELSE Pass")

print("\nRESULT: Basic classification logic demonstrated.")
