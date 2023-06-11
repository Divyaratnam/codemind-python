n=int(input())
a=list(map(int,input().split()))
c=0
l=[]
for i in a:
    if i==a.count(i):
        l.append(i)
l=list(set(l))
print(len(l))