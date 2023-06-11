n=int(input())
a=list(map(int,input().split()))
l=[]
for i in a:
    if i==a.count(i):
        l.append(i)
l=list(set(l))
if l==[]:
    print(-1)
else:
    print(min(l),max(l))