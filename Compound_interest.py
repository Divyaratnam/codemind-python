from math import pow
p,r,t=map(int,input().split())
print(format(p*pow((1+(r/100)),t),".2f"))