repeat_num = int(input())
arr = []
for i in range(repeat_num):
    arr.append(int(input()))
arr.sort()

for sort_num in arr:
    print(sort_num)
