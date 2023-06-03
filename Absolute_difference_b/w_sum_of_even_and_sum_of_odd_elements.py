n=int(input())
a=list(map(int,input().split()))
o,e=0,0
for i in range(n):
    if a[i]%2!=0:
        o+=a[i]
    else:
        e+=a[i]
print(abs(o-e))