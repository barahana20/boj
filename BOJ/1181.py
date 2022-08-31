a = int(input())

b = list(set([input() for _ in range(a)]))

print(sorted(b.sort(), key=lambda x: len(x)))
