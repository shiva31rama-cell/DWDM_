# Simple k-means.
# We compare squared distances, so sqrt() is not needed.

points = [
    [1, 1], [2, 1], [1, 2],
    [8, 8], [9, 8], [8, 9]
]

centers = [[1, 1], [8, 8]]

for repeat in range(5):
    cluster1 = []
    cluster2 = []

    # Step 1: assign each point to the nearest center
    for point in points:
        d1 = (point[0] - centers[0][0]) ** 2 + (point[1] - centers[0][1]) ** 2
        d2 = (point[0] - centers[1][0]) ** 2 + (point[1] - centers[1][1]) ** 2

        if d1 <= d2:
            cluster1.append(point)
        else:
            cluster2.append(point)

    # Step 2: calculate new centers
    x1 = y1 = 0
    for point in cluster1:
        x1 = x1 + point[0]
        y1 = y1 + point[1]

    x2 = y2 = 0
    for point in cluster2:
        x2 = x2 + point[0]
        y2 = y2 + point[1]

    new_centers = [
        [x1 / len(cluster1), y1 / len(cluster1)],
        [x2 / len(cluster2), y2 / len(cluster2)]
    ]

    centers = new_centers

print("Cluster 1:", cluster1)
print("Cluster 2:", cluster2)
print("Centers:", centers)