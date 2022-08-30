import sys

a, b = map(int, sys.stdin.readline().split())
box_arr = []
for _ in range(b):
    box_arr.append(sys.stdin.readline().split())

def aaa(a,b):
    tomato_zone = []
    no_tomato_zone = []
    for i in range(b):
        for j in range(a):
            if box_arr[i][j] == '1':
                tomato_zone.append([i,j])
            elif box_arr[i][j] == '-1':
                no_tomato_zone.append([i,j])
    day_count = 0
    visited = []
    while True:
        for i in range(b):
            for j in range(a):
                if [i, j] in tomato_zone and [i, j] not in visited:
                    right = [i, j+1]
                    left = [i, j-1]
                    down = [i+1, j]
                    up = [i-1, j]
                    visited.append([i, j])
                    print([i,j])
                    
                    if j<a-1 and right not in no_tomato_zone and right not in tomato_zone and i < b-1 and down not in no_tomato_zone and down not in tomato_zone and j > 0 and left not in no_tomato_zone and left not in tomato_zone and i > 0 and up not in no_tomato_zone and up not in tomato_zone:
                        return day_count
                    if j<a-1 and right not in no_tomato_zone and right not in tomato_zone:
                        tomato_zone.append(right)
                    if i < b-1 and down not in no_tomato_zone and down not in tomato_zone:
                        tomato_zone.append(down)
                    if j > 0 and left not in no_tomato_zone and left not in tomato_zone:
                        tomato_zone.append(left)
                    if i > 0 and up not in no_tomato_zone and up not in tomato_zone:
                        tomato_zone.append(up)
                    day_count+=1
                elif [0,0] in visited:
                    return day_count
                else:
                    continue
print(aaa(a,b))