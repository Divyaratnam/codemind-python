n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(n):
    if(a[i]==0):
        c+=1
for i in range(c):
    a[i]=0
    print(0,end=' ')
for i in range(c,n):
    a[i]=1
    print(1,end=' ')