a = int(input())

def append_array(arr, i):
    arr = list()
    arr.append(i)
    return arr
b = [input() for _ in range(a)]

dic = {}

for i in b:
    dic[len(i)] = []

for i in b:
    dic[len(i)].append(i)

print(dic)