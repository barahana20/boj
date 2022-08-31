b = list(set([input() for _ in range(int(input()))]))
b.sort()
print('\n'.join(sorted(b, key=lambda x: len(x))))