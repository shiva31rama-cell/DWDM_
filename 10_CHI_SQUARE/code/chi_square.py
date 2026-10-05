observed = [
    [30, 20],
    [10, 40],
]

row_totals = [sum(row) for row in observed]
col_totals = [sum(observed[r][c] for r in range(len(observed))) for c in range(len(observed[0]))]
total = sum(row_totals)

chi_square = 0.0
for r in range(len(observed)):
    for c in range(len(observed[0])):
        expected = row_totals[r] * col_totals[c] / total
        chi_square += (observed[r][c] - expected) ** 2 / expected

print("Observed table:", observed)
print("Chi-square value =", round(chi_square, 4))