import numpy as np
rows=int(input())
cols=int(input())
matrix = [list(map(int, input().split())) for _ in range(rows)]
mat=np.array(matrix)
rows, cols = np.where(mat == 0)
if rows.size > 0 and cols.size > 0:
    mat[rows, :] = 0
    mat[:, cols] = 0
for i in range(len(matrix)):
    matrix[i][:] = mat[i].tolist()
print(matrix)