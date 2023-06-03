n=int(input())
ar=list(map(int,input().split()))
a=sum(ar)//len(ar)
if a in ar:
    print(True)
else:
    print(False)