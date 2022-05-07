import sys

repeat_num = int(input())
arr = []
for i in range(repeat_num):
    arr.append(int(sys.stdin.readline()))
arr.sort()

for sort_num in arr:
    print(sort_num)
