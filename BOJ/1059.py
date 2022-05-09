input()
a = list(map(int, input().split()))
b = int(input())
a.append(b)
c = sorted(a)
count = 0
if c.index(b) == 0:
    for i in range(1,b+1):
        for j in range(b, c[c.index(b)+1]):
            if i==j:
                continue
            count+=1

else:
    for i in range(c[c.index(b)-1]+1,b+1):
        for j in range(b,c[c.index(b)+1]):
            if i==j:
                continue
            count+=1
print(count)