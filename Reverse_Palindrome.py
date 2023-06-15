def reverse(n):
    r=0
    while(n!=0):
        r=r*10+n%10
        n//=10
    return r
n=int(input())
k=n
while(1):
    re=reverse(n)
    k+=re
    n=k
    p=reverse(n)
    if k==p:
        print(k)
        break