n=int(input())
l=list(map(int,input().split()))
m=min(l)
e=0
c=0
while(m!=0):
    c+=1
    m//=10
for i in l:
    d=0
    while i!=0:
        d+=1
        i//=10
    if d==c:
       e+=1
print(e)