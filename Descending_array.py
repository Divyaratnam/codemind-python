n=int(input())
a=list(map(int,input().split()))
if a==sorted(a,reverse=True):
    print('yes')
else:
    print('no')