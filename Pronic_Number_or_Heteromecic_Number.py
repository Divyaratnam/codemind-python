n=int(input())
for i in range(int(n**0.5)+1):
    if i*(i+1)==n:
        print("YES")
        break
else:
    print("NO")