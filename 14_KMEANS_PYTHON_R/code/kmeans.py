import math

points = [(1, 1), (1.5, 2), (2, 1.5), (8, 8), (8.5, 9), (9, 8.5)]
centroids = [(1, 1), (8, 8)]

def distance(a, b):
    return math.sqrt(sum((x-y)**2 for x, y in zip(a, b)))

for _ in range(10):
    clusters = [[], []]
    for point in points:
        index = min(range(2), key=lambda i: distance(point, centroids[i]))
        clusters[index].append(point)

    new_centroids = []
    for i, cluster in enumerate(clusters):
        if cluster:
            new_centroids.append(tuple(sum(p[d] for p in cluster) / len(cluster) for d in range(2)))
        else:
            new_centroids.append(centroids[i])

    if new_centroids == centroids:
        break
    centroids = new_centroids

print("Clusters:", clusters)
print("Centroids:", centroids)