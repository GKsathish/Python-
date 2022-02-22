m, n = map(int, input().split())
matrix = [[int(x) for x in input().split()] for _ in range(m)]
new_matrix = [matrix[i][:] for i in range(m)]
for i in range(m):
    
    for j in range(n):
        if not matrix[i][j]:
            new_matrix[i] = [0] * n
            for k in range(m):
                new_matrix[k][j] = 0
for i in range(m):
    for j in range(n):
        if not matrix[i][j]:
            new_matrix[i][j] = matrix[i][max(j - 1, 0)] + matrix[i][min(j + 1, n - 1)] + matrix[max(i - 1, 0)][j] + \
                               matrix[min(i + 1, m - 1)][j]
for i in range(m):
    print(*new_matrix[i])