N=int(input())
m1=0
m2=0
for i in range(1,N):
    lia=[]
    stra=str(i)
    if (stra==(stra[::-1])):
        lia.append(i)
        m1=lia[-1]
    for i in range(N+1,N*N):
        lia=[]
        stra1=str(i)
        if (stra1==(stra1[::-1])):
            lia.append(i)
            m2=lia[0]
            break
res1=N-int(m1)
res2=abs(int(m2)-N)
if (res2<res1):
    print(int(m2))
elif(res2==res1):
    print(int(m1))
else:
    print(int(m1))
    
