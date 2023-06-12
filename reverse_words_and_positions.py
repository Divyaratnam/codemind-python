s=list(map(str,input().split()))
r=[]
for i in range(len(s)):
    r.append(s[i][len(s[i])::-1])
for i in range(len(r)-1,-1,-1):
    print(r[i],end=' ')