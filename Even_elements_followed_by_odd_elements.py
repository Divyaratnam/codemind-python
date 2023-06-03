n=int(input())
arr=list(map(int,input().split()))
e=[]
for i in range(n):
    if arr[i]%2==0:
        e.append(arr[i])
for i in range(n):
    if arr[i]%2!=0:
        e.append(arr[i])
print(' '.join(map(str,e)))