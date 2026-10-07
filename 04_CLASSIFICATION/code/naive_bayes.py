# 1. Training data
data = [
    ["Sunny", "Hot", "No"],
    ["Sunny", "Cool", "Yes"],
    ["Rainy", "Cool", "Yes"],
    ["Rainy", "Hot", "Yes"],
    ["Cloudy", "Hot", "Yes"],
    ["Cloudy", "Cool", "Yes"]
]

# Test record
test_weather = "Rainy"
test_temperature = "Hot"

# 2. Count class values
yes_count = 0
no_count = 0

for row in data:
    if row[2] == "Yes":
        yes_count = yes_count + 1
    else:
        no_count = no_count + 1

# 3. Count matching attribute values
yes_weather = 0
yes_temperature = 0
no_weather = 0
no_temperature = 0

for row in data:
    if row[2] == "Yes":
        if row[0] == test_weather:
            yes_weather = yes_weather + 1
        if row[1] == test_temperature:
            yes_temperature = yes_temperature + 1
    else:
        if row[0] == test_weather:
            no_weather = no_weather + 1
        if row[1] == test_temperature:
            no_temperature = no_temperature + 1

# 4. Calculate probabilities
p_yes = (yes_count / len(data))
p_yes = p_yes * ((yes_weather + 1) / (yes_count + 3))
p_yes = p_yes * ((yes_temperature + 1) / (yes_count + 2))

p_no = (no_count / len(data))
p_no = p_no * ((no_weather + 1) / (no_count + 3))
p_no = p_no * ((no_temperature + 1) / (no_count + 2))

# 5. Display result
print("P(Yes) =", p_yes)
print("P(No)  =", p_no)

if p_yes > p_no:
    print("Predicted class = Yes")
else:
    print("Predicted class = No")
