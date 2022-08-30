import sys

a, b = map(int, sys.stdin.readline().split())
box_arr = []
for _ in range(b):
    box_arr.append(sys.stdin.readline().split())

tomato_zone = []
no_tomato_zone = []
for i in range(b):
    for j in range(a):
        if box_arr[i][j] == '1':
            tomato_zone.append([i,j])
        elif box_arr[i][j] == '-1':
            no_tomato_zone.append([i,j])
day_count = 0
right = [i, j+1]
left = [i, j-1]
down = [i+1, j]
up = [i-1, j]
for i in range(b):
    for j in range(a):
        if j<a-1 and right not in no_tomato_zone and right not in tomato_zone:
            tomato_zone.append(right)
        elif i < b-1 and down not in no_tomato_zone and down not in tomato_zone:
            tomato_zone.append(down)
        elif j > 0 and left not in no_tomato_zone and left not in tomato_zone:
            tomato_zone.append(left)
        elif i > 0 and up not in no_tomato_zone and up not in tomato_zone:
            tomato_zone.append(up)
        day_count+=1
print(day_count)