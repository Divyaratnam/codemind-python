n=int(input())
ar=list(map(int,input().split()))
a,b=map(int,input().split())
l=[]
for i in ar:
    if i>=a and i<=b:
        l.append(i)
print(sum(l))