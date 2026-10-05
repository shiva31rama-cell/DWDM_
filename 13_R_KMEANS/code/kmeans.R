data <- data.frame(
  x = c(1, 1.5, 2, 8, 8.5, 9),
  y = c(1, 2, 1.5, 8, 9, 8.5)
)

set.seed(42)
model <- kmeans(data, centers = 2, nstart = 10)

print(model$cluster)
print(model$centers)