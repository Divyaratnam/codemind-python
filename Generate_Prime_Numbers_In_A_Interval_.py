a=int(input())
b=int(input())
for i in range(a+1,b+1):
    for j in range(2,i//2+1):
        if i%j==0:
            break
    else:
        print(i)