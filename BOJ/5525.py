N = int(input())
M = int(input())
c = input()
def recursive_func():
    global count
    global index
    if c[index:index+2] == 'OI':
        index += 2
        count += 1
        recursive_func()
string = 'I'+'OI'*N
index = 0
count = 0

while index < M:
    if c[index:index+(2*N+1)] == string:
        index += 2*N+1
        count+=1
        if c[index:index+2] == 'OI':
            recursive_func()
    else:
        index+=1
print(count)