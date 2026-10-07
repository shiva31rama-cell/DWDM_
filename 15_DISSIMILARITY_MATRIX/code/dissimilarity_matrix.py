import math

# 1. Create a dataset with four instances and two attributes
points = [
    [1, 2],
    [2, 4],
    [5, 5],
    [8, 7]
]

# 2. Calculate Euclidean dissimilarity
def distance(a, b):
    value = (a[0] - b[0]) ** 2
    value = value + (a[1] - b[1]) ** 2
    return math.sqrt(value)

# 3. Create the dissimilarity matrix
matrix = []

for i in range(len(points)):
    row = []

    for j in range(len(points)):
        row.append(distance(points[i], points[j]))

    matrix.append(row)

# 4. Display the matrix
print("--- DISSIMILARITY MATRIX ---")

for row in matrix:
    for value in row:
        print("%.2f" % value, end=" ")
    print()

# 5. Observation
print("\nObservation: The diagonal values are 0 because")
print("the dissimilarity of an object with itself is 0.")
