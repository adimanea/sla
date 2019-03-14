# import numpy as np

litere = ["a", "b", "c", "d", "e"]

rows, cols = 5, 5
mat = [[[0, 0] for c in range(cols)] for r in range(rows)]
for i in range(5):
    for j in range(5):
        mat[i][j] = litere[i]
        print(mat[i][j], end=" ")
    print()
print("##################################################")


def column(matrix, i):
    return [row[i] for row in matrix]


length = 5
for i in range(3):
    for j in mat[i]:
        if "b" in j:
            del mat[i]
            length -= 1
print(mat)
