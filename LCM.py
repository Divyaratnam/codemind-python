a,b=map(int,input().split())
c=max(a,b)
if c%a==0:
    print(c)
else:
    i=2
    while(1):
        if(c*i)%a==0:
            print(c*i)
            break
        i+=1