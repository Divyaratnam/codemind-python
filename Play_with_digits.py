n=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
    while(i!=0):
        s+=(i%10)
        i//=10
print(s)