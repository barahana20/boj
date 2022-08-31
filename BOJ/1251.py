a = input()

for i in range(1, len(a)-2):
    for j in range(i+1, len(a)-1):
        print(a[0:i], a[i:j], a[j+1:])