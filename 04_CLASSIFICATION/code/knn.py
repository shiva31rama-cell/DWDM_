# Very small k-NN example using only loops.
# Points are [height, weight, class].

data = [
    [150, 45, "A"],
    [155, 50, "A"],
    [160, 52, "A"],
    [175, 70, "B"],
    [180, 75, "B"],
    [185, 80, "B"]
]

test = [158, 51]
k = 3

distances = []

for row in data:
    # Squared Euclidean distance
    distance = (row[0] - test[0]) ** 2 + (row[1] - test[1]) ** 2
    distances.append([distance, row[2]])

# Simple selection sort: smallest distance first
for i in range(len(distances)):
    for j in range(i + 1, len(distances)):
        if distances[j][0] < distances[i][0]:
            temp = distances[i]
            distances[i] = distances[j]
            distances[j] = temp

count_a = 0
count_b = 0

for i in range(k):
    if distances[i][1] == "A":
        count_a += 1
    else:
        count_b += 1

print("Nearest classes:")
for i in range(k):
    print(distances[i][1])

if count_a > count_b:
    print("Predicted class = A")
else:
    print("Predicted class = B")