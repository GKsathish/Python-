# s=a4b3c2
# o=aaaabbbcc
stri='a4b3c2'
out=''
for ch in stri:
    if ch.isalpha():
        x=ch
    else:
        digit=int(ch)
        out=out+x*digit
print(out)


stri=input()
out=''
for ch in stri:
    if ch.isalpha():
        x=ch
    else:
        digit=int(ch)
        out=out+x*digit
        jo=''.join(sorted(out))
print(jo)



