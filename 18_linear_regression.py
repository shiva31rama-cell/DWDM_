# EXPERIMENT 18 - LINEAR REGRESSION
# No external package is needed.
# Dataset:
# X = study hours
# Y = marks
#
# Model:
# y = a + b*x
# b = slope
# a = intercept

x = [1, 2, 3, 4, 5]
y = [35, 40, 50, 55, 65]

n = len(x)

sum_x = 0
sum_y = 0
sum_xy = 0
sum_x2 = 0

for i in range(n):
    sum_x = sum_x + x[i]
    sum_y = sum_y + y[i]
    sum_xy = sum_xy + x[i] * y[i]
    sum_x2 = sum_x2 + x[i] * x[i]

# Calculate slope b.
b = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x * sum_x)

# Calculate intercept a.
a = (sum_y - b * sum_x) / n

print("Slope b =", round(b, 2))
print("Intercept a =", round(a, 2))

new_x = 6
predicted_y = a + b * new_x

print("For", new_x, "study hours:")
print("Predicted marks =", round(predicted_y, 2))

print("\nRESULT: Simple linear regression completed.")
