import sys
student = {}
repeat_num = int(sys.stdin.readline())
for i in range(repeat_num):
    input_data = sys.stdin.readline().split()
    student[input_data[0]] = [int(input_data[1]), int(input_data[2]), int(input_data[3])]

b = sorted(student.items(), key=lambda x: (-x[1][0], x[1][1], -x[1][2], x[0]))

for i in b:
    print(i[0])