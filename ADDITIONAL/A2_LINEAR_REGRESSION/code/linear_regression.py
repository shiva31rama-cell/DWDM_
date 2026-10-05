# Simple linear regression: y = b0 + b1*x

x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]

n = len(x)
mean_x = sum(x) / n
mean_y = sum(y) / n

numerator = sum((x[i]-mean_x)*(y[i]-mean_y) for i in range(n))
denominator = sum((value-mean_x)**2 for value in x)

b1 = numerator / denominator
b0 = mean_y - b1 * mean_x

print(f"Intercept (b0) = {b0:.4f}")
print(f"Slope (b1) = {b1:.4f}")

x_new = 6
print(f"Prediction for x={x_new}: {b0 + b1*x_new:.4f}")