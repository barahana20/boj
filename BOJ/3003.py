arr = [1,1,2,2,2,8]
arr1 = map(int, input().split())
for i, j in zip(arr,arr1):
    print(i-j, end=' ')