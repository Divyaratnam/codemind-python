n=int(input())
a=list(map(int,input().split()))
l=[]
for i in a:
    if i!=1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            l.append(i)
print("%.2f"%(sum(l)/len(l)))