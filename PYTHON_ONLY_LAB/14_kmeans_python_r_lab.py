# EXPERIMENT 14 - K-MEANS USING PYTHON
# No external package is needed.
# Dataset = six 2D points.
# K = 3.
#
# Steps: choose centroids -> assign points -> update centroids -> repeat.

import math

points = [
    [1, 1], [2, 1],
    [8, 8], [9, 8],
    [5, 5], [6, 5]
]

centroids = [
    [1, 1],
    [8, 8],
    [5, 5]
]

for iteration in range(4):
    clusters = [[], [], []]

    for point in points:
        best_cluster = 0

        best_distance = math.sqrt(
            (point[0] - centroids[0][0]) ** 2 +
            (point[1] - centroids[0][1]) ** 2
        )

        distance1 = math.sqrt(
            (point[0] - centroids[1][0]) ** 2 +
            (point[1] - centroids[1][1]) ** 2
        )

        if distance1 < best_distance:
            best_distance = distance1
            best_cluster = 1

        distance2 = math.sqrt(
            (point[0] - centroids[2][0]) ** 2 +
            (point[1] - centroids[2][1]) ** 2
        )

        if distance2 < best_distance:
            best_cluster = 2

        clusters[best_cluster].append(point)

    for c in range(3):
        if len(clusters[c]) > 0:
            sum_x = 0
            sum_y = 0

            for point in clusters[c]:
                sum_x = sum_x + point[0]
                sum_y = sum_y + point[1]

            centroids[c] = [
                sum_x / len(clusters[c]),
                sum_y / len(clusters[c])
            ]

for i in range(3):
    print("Cluster", i + 1, "=", clusters[i])
    print("Centroid", i + 1, "=", centroids[i])

print("\nRESULT: Simple K-Means completed.")
