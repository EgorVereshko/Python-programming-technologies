size = int(input())

matrix = [[i + 1 for i in range(size)] for _ in range(size)]

for row in matrix:
    print(row)

for i in range(size):
    for j in range(i + 1, size):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

for row in matrix:
    print(row)