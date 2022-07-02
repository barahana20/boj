while True:
    a = input()
    if a == '#':
        break
    result = 0
    for i in ['a', 'e', 'i', 'o', 'u']:
        result += a.lower().count(i)
    print(result)

