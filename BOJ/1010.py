def factorial(n,r):
    d = 1
    for i in range(n-(r-1),n+1,1):
        if i==0:
            continue
        d*=i
    return d
def factorial1(r):
    d = 1
    for i in range(1,r+1,1):
        d*=i
    return d
repeat_num = int(input())
for i in range(repeat_num):
    n,r = map(int, input().split())
    n,r = [max(n,r), min(n,r)]
    print(factorial(n, r)//factorial1(r))