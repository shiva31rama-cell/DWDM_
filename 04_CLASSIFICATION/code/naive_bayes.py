# Very simple Naive Bayes for two categorical attributes.
# No ML library is used.

data = [
    ["Sunny", "Hot", "No"],
    ["Sunny", "Cool", "Yes"],
    ["Rainy", "Cool", "Yes"],
    ["Rainy", "Hot", "Yes"],
    ["Cloudy", "Hot", "Yes"],
    ["Cloudy", "Cool", "Yes"]
]

test_weather = "Rainy"
test_temperature = "Hot"

yes_count = 0
no_count = 0

for row in data:
    if row[2] == "Yes":
        yes_count += 1
    else:
        no_count += 1

yes_weather = 0
yes_temp = 0
no_weather = 0
no_temp = 0

for row in data:
    if row[2] == "Yes":
        if row[0] == test_weather:
            yes_weather += 1
        if row[1] == test_temperature:
            yes_temp += 1
    else:
        if row[0] == test_weather:
            no_weather += 1
        if row[1] == test_temperature:
            no_temp += 1

# Simple probability with Laplace smoothing.
yes_probability = (yes_count / len(data)) * ((yes_weather + 1) / (yes_count + 3)) * ((yes_temp + 1) / (yes_count + 2))
no_probability = (no_count / len(data)) * ((no_weather + 1) / (no_count + 3)) * ((no_temp + 1) / (no_count + 2))

print("Yes probability =", yes_probability)
print("No probability =", no_probability)

if yes_probability > no_probability:
    print("Predicted class = Yes")
else:
    print("Predicted class = No")