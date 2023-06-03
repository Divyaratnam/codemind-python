def even_e_even(arr):
    c=0
    for i in range(1,len(arr)-1):
        if arr[i]%2==0 and arr[i-1]%2==0 and arr[i+1]%2==0:
         c+=1
    return c
n=int(input())
arr=list(map(int,input().split()))
print(even_e_even(arr))