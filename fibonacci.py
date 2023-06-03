n=int(input())
a=0
b=1
c=a+b
if n==1:
    print(a,end=' ')
elif n==2:
    print(a,b,end=' ')
else:
    print(a,b,end=' ')
    for i in range (3,n+1):
        print(c,end=' ')
        a=b
        b=c
        c=a+b