# 1. Create sample data
data <- data.frame(
  x = c(1, 1.5, 2, 8, 8.5, 9),
  y = c(1, 2, 1.5, 8, 9, 8.5)
)

print("--- INPUT DATA ---")
print(data)

# 2. Set the random seed
set.seed(42)

# 3. Apply simple K-Means with 2 clusters
model <- kmeans(
  data,
  centers = 2,
  nstart = 10
)

# 4. Display cluster assignment
print("--- CLUSTER ASSIGNMENT ---")
print(model$cluster)

# 5. Display cluster centers
print("--- CLUSTER CENTERS ---")
print(model$centers)

# 6. Observation
print("Observation: The data is divided into two clusters.")
