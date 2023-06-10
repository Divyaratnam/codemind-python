n=int(input())
a=set(map(int,input().split()))
s=0
for i in a:
    if i%2==1:
        s+=i
print(s)