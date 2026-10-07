# EXPERIMENT 07 - ZEROR CLASSIFIER
# ZeroR ignores all input attributes.
# It always predicts the majority class.
# No external package is needed.
#
# Dataset = [study_hours, result]

data = [
    [2, "Pass"],
    [4, "Pass"],
    [5, "Fail"],
    [3, "Pass"],
    [6, "Pass"],
    [1, "Pass"]
]

pass_count = 0
fail_count = 0

for row in data:
    if row[1] == "Pass":
        pass_count = pass_count + 1
    else:
        fail_count = fail_count + 1

print("Pass count =", pass_count)
print("Fail count =", fail_count)

if pass_count > fail_count:
    prediction = "Pass"
else:
    prediction = "Fail"

print("ZeroR prediction =", prediction)

correct = 0
for row in data:
    if row[1] == prediction:
        correct = correct + 1

accuracy = correct / len(data) * 100
print("Accuracy =", round(accuracy, 2), "%")

print("\nRESULT: ZeroR selected the majority class.")
