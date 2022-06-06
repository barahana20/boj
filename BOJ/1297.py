import math

a,b,c = map(int,input().split())
d=math.sqrt(b**2+c**2)
print(int(a/d*b),int(a/d*c))