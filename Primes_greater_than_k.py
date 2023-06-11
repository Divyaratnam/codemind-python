n=int(input())
a=list(map(int,input().split()))
k=int(input())
l=[]
c=0
for i in a:
    for j in range(2,i):
        if i%j==0:
            break
    else:
        l.append(i)
for i in l:
    if i>=k:
        c+=1
print(c)