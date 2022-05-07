a,b = map(int, input().split())
for i in [c-b*a for c in list(map(int, input().split()))]:
    print(i,end=' ')