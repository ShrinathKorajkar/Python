def find(mat1, mat2, i, j, visited, step, r, c):

    step += 1
    if visited[i][j] == visited[-1][-1]:
        print(step)
        return step - 1
    elif (i + mat1[i][j]) < r and (j + mat2[i][j]) < c:
        return min(find(mat1, mat2, i + mat1[i][j], j, visited, step, r, c),
                   find(mat1, mat2, i, j + mat2[i][j], visited, step, r, c))

    elif (i + mat1[i][j]) < r:
        return find(mat1, mat2, i + mat1[i][j], j, visited, step, r, c)
    elif (j + mat2[i][j]) < c:
        return find(mat1, mat2, i, j + mat2[i][j], visited, step, r, c)
    else:
        return step - 1


R, C = list(map(int, input().split()))
matrix1 = []
matrix2 = []
visited = []
for _ in range(R):
    visited.append(list(0 for i in range(C)))
for i in range(R):
    matrix1.append(list(map(int, input().split())))
for i in range(R):
    matrix2.append(list(map(int, input().split())))

visited[-1][-1] = 2
print(find(matrix1, matrix2, 0, 0, visited, 0, R, C))
