# Python version of the same simple k-means idea used in the R experiment.

points = [[1, 1], [2, 1], [1, 2], [8, 8], [9, 8], [8, 9]]
center1 = [1, 1]
center2 = [8, 8]

for repeat in range(5):
    cluster1 = []
    cluster2 = []

    for p in points:
        d1 = (p[0] - center1[0]) ** 2 + (p[1] - center1[1]) ** 2
        d2 = (p[0] - center2[0]) ** 2 + (p[1] - center2[1]) ** 2

        if d1 <= d2:
            cluster1.append(p)
        else:
            cluster2.append(p)

    x = y = 0
    for p in cluster1:
        x += p[0]
        y += p[1]
    center1 = [x / len(cluster1), y / len(cluster1)]

    x = y = 0
    for p in cluster2:
        x += p[0]
        y += p[1]
    center2 = [x / len(cluster2), y / len(cluster2)]

print("Cluster 1:", cluster1)
print("Cluster 2:", cluster2)
print("Center 1:", center1)
print("Center 2:", center2)