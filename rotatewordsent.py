s = input()
n = int(input())
words = s.split()
lengths = [len(w) for w in words]
s = ''.join(words)
s = s[n:] + s[:-n]
res = ''
i = 0
for l in lengths:
    if res:
        res += ' '
    res += s[i:i+l]
    i += l
print(res)