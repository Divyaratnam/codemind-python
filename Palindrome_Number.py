def palin(n):
    k=str(n)
    if n==int(k[-1::-1]):
        return True
    else:
        return False
t=int(input())
for i in range(1,t+1):
    n=int(input())
    if palin(n):
        print(True)
    else:
        print(False)