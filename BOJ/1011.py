import math


repeat_num = int(input())
for _ in range(repeat_num):
    x,y = map(int,input().split())
    distance = y-x
    
    print(math.ceil(math.sqrt(distance)))