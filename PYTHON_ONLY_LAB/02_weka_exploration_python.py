# EXPERIMENT 02 - WEKA DATASET EXPLORATION (PYTHON PRACTICE)
# Actual WEKA exploration is a GUI/tool activity.
# This Python file demonstrates the same basic ideas.
# No external package is needed.
#
# Dataset:
# study_hours -> numeric attribute
# attendance  -> numeric attribute
# result      -> class attribute

data = [
    [2, 70, "Fail"],
    [4, 80, "Pass"],
    [5, 85, "Pass"],
    [1, 60, "Fail"],
    [6, 90, "Pass"],
    [3, 75, "Pass"]
]

print("DATASET")
for row in data:
    print(row)

print("\nATTRIBUTES")
print("study_hours : Numeric")
print("attendance  : Numeric")
print("result      : Nominal / Class")

print("\nTOTAL RECORDS =", len(data))

pass_count = 0
fail_count = 0

for row in data:
    if row[2] == "Pass":
        pass_count = pass_count + 1
    else:
        fail_count = fail_count + 1

print("Pass records =", pass_count)
print("Fail records =", fail_count)

print("\nSIMPLE STUDY-HOURS FREQUENCY")
hour_count = {}

for row in data:
    hours = row[0]
    if hours not in hour_count:
        hour_count[hours] = 0
    hour_count[hours] = hour_count[hours] + 1

for hours in sorted(hour_count):
    print(hours, "hour(s):", hour_count[hours])

print("\nRESULT: Dataset attributes, types and class counts inspected.")
print("NOTE: Use WEKA for the actual Explorer/Knowledge Flow GUI work.")
