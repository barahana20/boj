repeat_num = int(input())

a = []

for _ in range(repeat_num):
    a.append(input())
if repeat_num == 1:
    for i in a:
        print(i, end='')
else:
    d = []
    for i in range(len(a[0])):
        for j in range(len(a)):
            if j == 0:
                e = a[j][i]
            elif j < len(a)-1:
                if e == a[j][i]:
                    e = a[j][i]
                    continue
                else:
                    e = a[j][i]
                    break
            else:
                if e == a[j][i]:
                    d.append(i)
                else:
                    break
    arr = []
    for _ in range(len(a[0])):
        arr.append(False)
    for i in d:
        arr[i] = a[0][i]
    for i in sorted(list(set([i for i in range(len(a[0]))])-set(d))):
        arr[i] = '?'

    for i in arr:
        print(i, end='')