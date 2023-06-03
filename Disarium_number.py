import math
n=list(input())
nu=int(''.join(n))
s=0
j=1
for i in n:
   s+=math.pow(int(i),j)
   j+=1
if s==nu:
    print(True)
else:
    print(False)