n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
sum_first_diagonal = sum(a[i][i] for i in range(n))
sum_second_diagonal = 0
for i in range(n):
    for j in range(n):
        if i + j == n - 1:
            sum_second_diagonal += a[i][j]
if n % 2 == 0:
    sum = sum_first_diagonal + sum_second_diagonal
else:
    sum = sum_first_diagonal + sum_second_diagonal - a[int((n - 1)
                                                        / 2)][int((n - 1) / 2)]
print(sum)