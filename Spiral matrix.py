row=int(input())
col=int(input())
matrix=[list(map(int, input().split())) for _ in range(row)]
result = []
while matrix:
    result += matrix.pop(0)
    if matrix and matrix[0]:
        for row in matrix:
            result.append(row.pop())
    if matrix:
        result += matrix.pop()[::-1]
    if matrix and matrix[0]:
        for row in matrix[::-1]:
            result.append(row.pop(0))
print(result)