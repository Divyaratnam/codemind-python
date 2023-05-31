a=int(input())
k=a*a
s=0
while k>0:
    r=k%10
    s+=r
    k=k//10
if s==a:
    print('Neon Number')
else:
    print('Not Neon Number')