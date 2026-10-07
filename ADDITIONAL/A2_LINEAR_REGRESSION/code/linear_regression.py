# 1. Training data
x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]

# 2. Calculate means
n = len(x)
mean_x = sum(x) / n
mean_y = sum(y) / n

# 3. Calculate slope
numerator = 0
denominator = 0

for i in range(n):
    numerator = numerator + (x[i] - mean_x) * (y[i] - mean_y)
    denominator = denominator + (x[i] - mean_x) ** 2

slope = numerator / denominator

# 4. Calculate intercept
intercept = mean_y - slope * mean_x

# 5. Predict a new value
new_x = 6
prediction = intercept + slope * new_x

# 6. Display result
print("Slope =", round(slope, 4))
print("Intercept =", round(intercept, 4))
print("Prediction for x =", new_x, ":", round(prediction, 4))
