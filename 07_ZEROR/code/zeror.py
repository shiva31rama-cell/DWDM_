# ZeroR: choose the class that occurs most often.

classes = ["Setosa", "Versicolor", "Setosa", "Virginica", "Setosa"]

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

if setosa >= versicolor and setosa >= virginica:
    majority = "Setosa"
elif versicolor >= virginica:
    majority = "Versicolor"
else:
    majority = "Virginica"

print("Setosa count =", setosa)
print("Versicolor count =", versicolor)
print("Virginica count =", virginica)
print("ZeroR prediction =", majority)