n=int(input())
arr=list(map(int,input().split()))
for i in range(n):
    if arr[i]==1 or arr[i]==0:
        pass
    else:
        print(False)
        break
else:
    print(True)