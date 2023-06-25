n=int(input())
for i in range(n//2):
    if i*(i+1)==n:
        print('YES')
        break
else:
    print('NO')