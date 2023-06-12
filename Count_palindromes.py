n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    j=i
    r=0
    while(i!=0):
        r=r*10+(i%10)
        i//=10
    if j==r:
        c+=1
print(c)