n=int(input())
arr=list(map(int,input().split()))
o=[]
for i in range(n):
    if arr[i]%2!=0:
        o.append(arr[i])
for i in range(n):
    if arr[i]%2==0:
        o.append(arr[i])
print(' '.join(map(str,o)))