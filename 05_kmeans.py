# EXPERIMENT 05 - K-MEANS CLUSTERING
# Library used: math
# math.sqrt() gives square root for distance calculation.
# Dataset = six 2D points.
# K = 2 clusters.

import math

points = [
    [1, 1], [2, 1], [1, 2],
    [8, 8], [9, 8], [8, 9]
]

centroids = [[1, 1], [8, 8]]

for iteration in range(3):
    cluster1 = []
    cluster2 = []

    # STEP 1: Assign each point to the nearest centroid.
    for point in points:
        d1 = math.sqrt((point[0] - centroids[0][0]) ** 2 +
                       (point[1] - centroids[0][1]) ** 2)

        d2 = math.sqrt((point[0] - centroids[1][0]) ** 2 +
                       (point[1] - centroids[1][1]) ** 2)

        if d1 <= d2:
            cluster1.append(point)
        else:
            cluster2.append(point)

    # STEP 2: Recalculate centroid 1.
    sum_x = 0
    sum_y = 0
    for point in cluster1:
        sum_x = sum_x + point[0]
        sum_y = sum_y + point[1]

    centroids[0] = [sum_x / len(cluster1), sum_y / len(cluster1)]

    # STEP 3: Recalculate centroid 2.
    sum_x = 0
    sum_y = 0
    for point in cluster2:
        sum_x = sum_x + point[0]
        sum_y = sum_y + point[1]

    centroids[1] = [sum_x / len(cluster2), sum_y / len(cluster2)]

print("Cluster 1 =", cluster1)
print("Cluster 2 =", cluster2)
print("Centroid 1 =", centroids[0])
print("Centroid 2 =", centroids[1])

print("\nRESULT: K-Means completed.")
