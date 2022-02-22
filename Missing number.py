N = input().split()
A = [int(i) for i in N  if int(i)<0] 
A.sort(reverse=True)
num = -1
for j in range(len(A)):
    if num > A[j]:
        break
    num = A[j] - 1
print(num) 