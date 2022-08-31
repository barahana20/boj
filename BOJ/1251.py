a = input()
arr = []
for i in range(1, len(a)-1):
    for j in range(i+1, len(a)):
        m,n,k = a[0:i], a[i:j], a[j:]
        arr.append(m[::-1]+n[::-1]+k[::-1])

arr.sort()
print(arr[0])
    