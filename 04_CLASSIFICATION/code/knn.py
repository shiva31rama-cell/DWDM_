# 1. Training data: Height, Weight, Class
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

# 2. Calculate distance from test point
distances = []

for row in data:
    distance = (row[0] - test[0]) ** 2
    distance = distance + (row[1] - test[1]) ** 2
    distances.append([distance, row[2]])

# 3. Sort distances using simple selection sort
for i in range(len(distances)):
    for j in range(i + 1, len(distances)):
        if distances[j][0] < distances[i][0]:
            temp = distances[i]
            distances[i] = distances[j]
            distances[j] = temp

# 4. Count the first k classes
count_a = 0
count_b = 0

for i in range(k):
    if distances[i][1] == "A":
        count_a = count_a + 1
    else:
        count_b = count_b + 1

# 5. Display result
print("--- NEAREST CLASSES ---")
for i in range(k):
    print(distances[i][1])

if count_a > count_b:
    print("Predicted class = A")
else:
    print("Predicted class = B")
