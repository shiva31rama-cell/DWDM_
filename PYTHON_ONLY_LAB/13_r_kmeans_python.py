# EXPERIMENT 13 - K-MEANS
# Python companion for the R lab experiment.
# Library used: math
# math.sqrt() is used for Euclidean distance.
# No machine-learning library is used.
#
# Dataset = six 2D points, K = 2.

import math

data = [
    [1, 2], [2, 1], [2, 3],
    [8, 9], [9, 8], [9, 10]
]

centroid1 = data[0]
centroid2 = data[3]

for step in range(3):
    cluster1 = []
    cluster2 = []

    for point in data:
        d1 = math.sqrt((point[0] - centroid1[0]) ** 2 +
                       (point[1] - centroid1[1]) ** 2)

        d2 = math.sqrt((point[0] - centroid2[0]) ** 2 +
                       (point[1] - centroid2[1]) ** 2)

        if d1 <= d2:
            cluster1.append(point)
        else:
            cluster2.append(point)

    sum_x = 0
    sum_y = 0
    for point in cluster1:
        sum_x = sum_x + point[0]
        sum_y = sum_y + point[1]
    centroid1 = [sum_x / len(cluster1), sum_y / len(cluster1)]

    sum_x = 0
    sum_y = 0
    for point in cluster2:
        sum_x = sum_x + point[0]
        sum_y = sum_y + point[1]
    centroid2 = [sum_x / len(cluster2), sum_y / len(cluster2)]

print("Cluster 1 =", cluster1)
print("Cluster 2 =", cluster2)
print("Centroid 1 =", centroid1)
print("Centroid 2 =", centroid2)

print("\nRESULT: K-Means completed.")
