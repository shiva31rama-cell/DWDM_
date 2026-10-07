# EXPERIMENT 10 - CHI-SQUARE VALUE
# No external package is needed.
# Dataset = observed frequency table.
# Rows    = Young, Old
# Columns = Apple, Orange
#
# Formula:
# Chi-square = sum((Observed - Expected)^2 / Expected)

observed = [
    [30, 20],
    [10, 40]
]

total = 0

for row in observed:
    for value in row:
        total = total + value

row_total = [0, 0]
column_total = [0, 0]

for i in range(2):
    for j in range(2):
        row_total[i] = row_total[i] + observed[i][j]
        column_total[j] = column_total[j] + observed[i][j]

chi_square = 0

print("OBSERVED =", observed)
print("\nEXPECTED VALUES")

for i in range(2):
    for j in range(2):
        expected = (row_total[i] * column_total[j]) / total

        contribution = ((observed[i][j] - expected) ** 2) / expected
        chi_square = chi_square + contribution

        print("Cell", i + 1, j + 1, "Expected =", round(expected, 2))

print("\nChi-Square =", round(chi_square, 4))
print("\nRESULT: Chi-Square value calculated.")
