import math

# 1. Create two data objects
A = [1, 2, 3, 4]
B = [2, 3, 4, 5]

# 2. Euclidean distance
sum_square = 0

for i in range(len(A)):
    difference = A[i] - B[i]
    sum_square = sum_square + difference * difference

euclidean = math.sqrt(sum_square)

# 3. Manhattan distance
manhattan = 0

for i in range(len(A)):
    manhattan = manhattan + abs(A[i] - B[i])

# 4. Cosine similarity
dot = 0
square_a = 0
square_b = 0

for i in range(len(A)):
    dot = dot + A[i] * B[i]
    square_a = square_a + A[i] * A[i]
    square_b = square_b + B[i] * B[i]

cosine = dot / (math.sqrt(square_a) * math.sqrt(square_b))

# 5. Pearson correlation
mean_a = sum(A) / len(A)
mean_b = sum(B) / len(B)

numerator = 0
part_a = 0
part_b = 0

for i in range(len(A)):
    numerator = numerator + (A[i] - mean_a) * (B[i] - mean_b)
    part_a = part_a + (A[i] - mean_a) ** 2
    part_b = part_b + (B[i] - mean_b) ** 2

pearson = numerator / math.sqrt(part_a * part_b)

# 6. Jaccard similarity
intersection = 0
union = 0

for value in A:
    if value in B:
        intersection = intersection + 1
    union = union + 1

for value in B:
    if value not in A:
        union = union + 1

jaccard = intersection / union

# 7. Display results
print("Euclidean Distance =", euclidean)
print("Manhattan Distance =", manhattan)
print("Cosine Similarity =", cosine)
print("Pearson Correlation =", pearson)
print("Jaccard Similarity =", jaccard)
