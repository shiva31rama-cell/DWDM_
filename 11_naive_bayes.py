# EXPERIMENT 11 - NAIVE BAYES CLASSIFICATION
# No external package is needed.
# Dataset:
# outlook = Sunny / Rainy / Overcast
# play    = Yes / No
#
# We use frequency counting so the calculation is easy to follow.

data = [
    ["Sunny", "No"],
    ["Sunny", "No"],
    ["Overcast", "Yes"],
    ["Rainy", "Yes"],
    ["Rainy", "Yes"],
    ["Sunny", "Yes"]
]

test_outlook = "Sunny"

yes_count = 0
no_count = 0

for row in data:
    if row[1] == "Yes":
        yes_count = yes_count + 1
    else:
        no_count = no_count + 1

yes_match = 0
no_match = 0

for row in data:
    if row[0] == test_outlook and row[1] == "Yes":
        yes_match = yes_match + 1

    if row[0] == test_outlook and row[1] == "No":
        no_match = no_match + 1

p_yes = yes_count / len(data)
p_no = no_count / len(data)

# +1 is Laplace smoothing.
p_sunny_yes = (yes_match + 1) / (yes_count + 3)
p_sunny_no = (no_match + 1) / (no_count + 3)

score_yes = p_yes * p_sunny_yes
score_no = p_no * p_sunny_no

print("Score for Yes =", round(score_yes, 4))
print("Score for No  =", round(score_no, 4))

if score_yes > score_no:
    print("Prediction = Yes")
else:
    print("Prediction = No")

print("\nRESULT: Naive Bayes classification completed.")
