n=int(input())
l=list(map(int,input().split()))
a=[]
for i in l:
    r=0
    while(i!=0):
        r=r*10+(i%10)
        i//=10
    a.append(r)
for i in a:
    print(i,end=' ')