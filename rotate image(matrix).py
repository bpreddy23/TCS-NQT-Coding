rows=int(input())
cols=int(input())
matrix = [list(map(int, input().split())) for _ in range(rows)]
for i in range(len(matrix)):
    for j in range(i + 1, len(matrix)):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
for row in matrix:
    row.reverse()
print(matrix)