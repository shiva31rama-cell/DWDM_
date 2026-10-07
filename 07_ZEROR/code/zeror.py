# 1. Create class values
classes = ["Setosa", "Versicolor", "Setosa", "Virginica", "Setosa"]

# 2. Count each class
setosa = 0
versicolor = 0
virginica = 0

for value in classes:
    if value == "Setosa":
        setosa = setosa + 1
    elif value == "Versicolor":
        versicolor = versicolor + 1
    else:
        virginica = virginica + 1

# 3. Find majority class
if setosa >= versicolor and setosa >= virginica:
    majority = "Setosa"
elif versicolor >= virginica:
    majority = "Versicolor"
else:
    majority = "Virginica"

# 4. Display result
print("Setosa count =", setosa)
print("Versicolor count =", versicolor)
print("Virginica count =", virginica)
print("ZeroR prediction =", majority)
