n=int(input())
a=list(map(int,input().split()))
k=int(input())
l=[]
for i in a:
    if a.count(i)==k:
        l.append(i)
l=list(set(l))
if l==[]:
    print(-1)
else:
    for i in l:
        print(i,end=' ')