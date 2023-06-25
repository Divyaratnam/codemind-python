def prime(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return 0
    else:
        return 1
n=int(input())
s=str(n)
r=int(s[-1::-1])
if prime(n)==1 and prime(r)==1:
    print('circular prime')
elif prime(n)==1 and prime(r)==0:
    print('prime but not a circular prime')
else:
    print('not prime')