n=int(input())
arr=list(map(int,input().split()))
c=n-1
s=0
for i in range(n):
    if arr[i]==1:
        s+=(2**c)
        c-=1
    else:
        c-=1
print(s)