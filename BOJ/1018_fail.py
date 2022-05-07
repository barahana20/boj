a,b = map(int, input().split())
arr = []
for i in range(a):
    arr.append(list(input()))
def a1(a,b, arr):
    count_list = []

    for x in range(a-7):
        for y in range(b-7):
            count = 0
            for i in range(8):
                for j in range(8):
                    if j == 0:
                        d = arr[x+i][y+j]
                    else:
                        if d == arr[x+i][y+j]:
                            count+=1
                            if d == 'B':
                                d = 'W'
                            else:
                                d = 'B'
                        else:
                            d = arr[x+i][y+j]
            count_list.append(count)
    return count_list

def a2(a,b, arr):
    count_list = []

    for x in range(a-7):
        for y in range(b-7):
            count = 0
            for i in range(8):
                for j in range(8):
                    if j == 0:
                        d = arr[x+i][y+j]
                    elif j == 1:
                        if d == arr[x+i][y+j]:
                            if d == 'B':
                                d = 'W'
                            else:
                                d = 'B'
                            continue
                    else:
                        if d == arr[x+i][y+j]:
                            count+=1
                            if d == 'B':
                                d = 'W'
                            else:
                                d = 'B'
                        else:
                            d = arr[x+i][y+j]
            count_list.append(count)
    return count_list

print(a1(a,b,arr)+a2(a,b,arr))