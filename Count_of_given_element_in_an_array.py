n=int(input())
a=list(map(int,input().split()))
s=int(input())
c=0
for i in range(n):
    if a[i]==s:
        c+=1
print(c)