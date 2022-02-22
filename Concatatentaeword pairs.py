def concatenate(ws,n):
	ln = len(ws)
	result = []
	for i in range(ln):
		for j in range(ln):
			if i == j:
				continue
			else:
				temp = ws[i] + ws[j]
				if len(temp) == n:
					result.append(temp)
	return(list(set(sorted(result,key=str.lower))))
s = input().split()
num = int(input())
words = concatenate(s, num)
for x in sorted(words):
	print(x)