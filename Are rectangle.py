spaceSeparatedIntegers = input().split(' ')
N = int(spaceSeparatedIntegers[0])
M = int(spaceSeparatedIntegers[1])


matrix = []
for i in range(0, N):
    matrix.append(input().split(' '))


maxArea = 0
for i in range(0, N):
    for j in range(0, M):
       if matrix[i][j] == 'X':
           for k in range(0, N - i):
               for l in range(0, M - j):
                   found = True
                   for p in range(0, k + 1):
                       for z in range(0, l + 1):
                           if matrix[i+p][j+z] != 'X':
                              found = False
                   if found:
                      maxArea = max(maxArea, (k + 1) * (l + 1))




print(str(maxArea))