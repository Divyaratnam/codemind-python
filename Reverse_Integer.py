def reve(n):
    k=str(n)
    return int(k[-1::-1])
n=int(input())
s=str(n)
if s[0]=='-':
    r=reve(int(s[1::]))
    print(-r)
else:
    r=reve(n)
    print(r)