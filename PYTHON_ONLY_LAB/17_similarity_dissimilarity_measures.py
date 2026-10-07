# EXPERIMENT 17 - SIMILARITY AND DISSIMILARITY MEASURES
# Library used: math
# math.sqrt() is used for square-root calculations.
# A and B are two data objects.
#
# Measures:
# Pearson, Cosine, Jaccard, Euclidean, Manhattan.

import math

A = [1, 2, 3, 4]
B = [2, 4, 6, 8]

# PEARSON CORRELATION
mean_A = sum(A) / len(A)
mean_B = sum(B) / len(B)

top = 0
bottom_A = 0
bottom_B = 0

for i in range(len(A)):
    x = A[i] - mean_A
    y = B[i] - mean_B

    top = top + x * y
    bottom_A = bottom_A + x * x
    bottom_B = bottom_B + y * y

pearson = top / math.sqrt(bottom_A * bottom_B)

# COSINE SIMILARITY
dot = 0
length_A = 0
length_B = 0

for i in range(len(A)):
    dot = dot + A[i] * B[i]
    length_A = length_A + A[i] * A[i]
    length_B = length_B + B[i] * B[i]

cosine = dot / (math.sqrt(length_A) * math.sqrt(length_B))

# JACCARD SIMILARITY
set_A = {"A", "B", "C"}
set_B = {"B", "C", "D"}

intersection = 0
union = 0

for item in ["A", "B", "C", "D"]:
    if item in set_A and item in set_B:
        intersection = intersection + 1

    if item in set_A or item in set_B:
        union = union + 1

jaccard = intersection / union

# EUCLIDEAN DISTANCE
euclidean = 0
for i in range(len(A)):
    euclidean = euclidean + (A[i] - B[i]) ** 2
euclidean = math.sqrt(euclidean)

# MANHATTAN DISTANCE
manhattan = 0
for i in range(len(A)):
    manhattan = manhattan + abs(A[i] - B[i])

print("Pearson =", round(pearson, 4))
print("Cosine  =", round(cosine, 4))
print("Jaccard =", round(jaccard, 4))
print("Euclidean =", round(euclidean, 4))
print("Manhattan =", round(manhattan, 4))

print("\nRESULT: Similarity and dissimilarity measures calculated.")
