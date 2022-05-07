import math

def return_max_and_min(num1, num2):
    return [max(num1, num2), min(num1, num2)]

count = int(input())

for i in range(count):
    a = map(int, input().split())
    x1, y1, r1, x2, y2, r2 = a
    r1, r2 = return_max_and_min(r1, r2)
    d = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    if r1+r2 < d:
        print(0)
    elif r1+r2 == d:
        print(1)
    elif r1+r2 > d and r1-r2 < d:
        print(2)
    elif x1==x2 and y1==y2 and r1==r2:
        print(-1)
    elif d == r1-r2:
        print(1)
    elif d < r1-r2:
        print(0)