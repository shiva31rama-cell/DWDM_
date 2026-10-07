# EXPERIMENT 15 - DISSIMILARITY MATRIX
# Library used: math
# math.sqrt() is used for Euclidean distance.
# Dataset = four objects with two numeric attributes.
#
# A = [1, 2]
# B = [2, 4]
# C = [5, 6]
# D = [7, 8]
#
# Euclidean distance:
# sqrt((x1-x2)^2 + (y1-y2)^2)

import math

data = [
    [1, 2],
    [2, 4],
    [5, 6],
    [7, 8]
]

names = ["A", "B", "C", "D"]

print("      A      B      C      D")

for i in range(len(data)):
    print(names[i], end="  ")

    for j in range(len(data)):
        dx = data[i][0] - data[j][0]
        dy = data[i][1] - data[j][1]

        distance = math.sqrt(dx * dx + dy * dy)

        print(round(distance, 2), end="   ")

    print()

print("\nRESULT: Dissimilarity matrix calculated.")
