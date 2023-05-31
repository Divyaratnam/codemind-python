a=int(input())
s=0
m=1
while a>0:
    r=a%10
    s+=r
    m*=r
    a=a//10
if s==m:
    print('Spy Number')
else:
    print('Not Spy Number')