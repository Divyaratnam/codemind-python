def is_ugly(n):
    if n<=0:
        return False
    while n%2==0:
        n//=2
    while n%3==0:
        n//=3
    while n%5==0:
        n//=5
    return n==1
def print_n(n):
    if is_ugly(n):
        print('Ugly Number')
    else:
        print('Not Ugly Number')
n=int(input())
print_n(n)