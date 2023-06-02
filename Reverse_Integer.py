n=int(input())
s=str(n)
if s[0]=='-':
    print(int('-'+s[:0:-1]))
else:
    print(int(s[::-1]))