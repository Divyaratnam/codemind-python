def count_odd_b_odd(arr):
    c=0
    for i in range(1,len(arr)-1):
        if (arr[i-1]%2==0 and arr[i+1]%2!=0) or (arr[i-1]%2!=0 and arr[i+1]%2==0):
            c+=1
    return c
n=int(input())
arr=list(map(int,input().split()))
print(count_odd_b_odd(arr))