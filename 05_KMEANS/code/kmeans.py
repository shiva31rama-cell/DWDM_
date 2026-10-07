# 1. Create sample data
points = [
    [1, 1], [2, 1], [1, 2],
    [8, 8], [9, 8], [8, 9]
]

# 2. Select initial cluster centers
centers = [[1, 1], [8, 8]]

# 3. Repeat assignment and update steps
for repeat in range(5):
    cluster1 = []
    cluster2 = []

    # Assign every point to the nearest center
    for point in points:
        d1 = (point[0] - centers[0][0]) ** 2
        d1 = d1 + (point[1] - centers[0][1]) ** 2

        d2 = (point[0] - centers[1][0]) ** 2
        d2 = d2 + (point[1] - centers[1][1]) ** 2

        if d1 <= d2:
            cluster1.append(point)
        else:
            cluster2.append(point)

    # Calculate new center of cluster 1
    x1 = 0
    y1 = 0
    for point in cluster1:
        x1 = x1 + point[0]
        y1 = y1 + point[1]

    # Calculate new center of cluster 2
    x2 = 0
    y2 = 0
    for point in cluster2:
        x2 = x2 + point[0]
        y2 = y2 + point[1]

    centers[0] = [x1 / len(cluster1), y1 / len(cluster1)]
    centers[1] = [x2 / len(cluster2), y2 / len(cluster2)]

# 4. Display clusters and centers
print("--- CLUSTER 1 ---")
print(cluster1)

print("--- CLUSTER 2 ---")
print(cluster2)

print("--- FINAL CENTERS ---")
print(centers)
