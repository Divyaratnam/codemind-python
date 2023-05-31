a=int(input())
b=int(input())
for i in range (a,b+1):
    k=i
    n=0
    c=0
    while i>0:
        r=i%10
        c=c+1
        if r!=0 and k%r==0:
            n=n+1
        i=i//10
    if c==n:
        print(k,end=' ')