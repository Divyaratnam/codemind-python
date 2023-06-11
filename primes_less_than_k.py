n=int(input())
a=list(map(int,input().split()))
k=int(input())
c=0
for i in a:
    if i!=1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            if i<=k:
                c+=1
print(c)