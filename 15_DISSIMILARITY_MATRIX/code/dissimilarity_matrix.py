import math

points = [(1, 2), (2, 4), (5, 5), (8, 7)]

def euclidean(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

matrix = [[euclidean(a, b) for b in points] for a in points]

print("Dissimilarity matrix:")
for row in matrix:
    print(" ".join(f"{value:.2f}" for value in row))