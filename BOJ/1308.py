y1,m1,d1 = map(int, input().split())
y2,m2,d2 = map(int, input().split())
D_day = 0

m_list = {1:31, 2:28, 3:31, 4:30, 5:31, 6:31, 7:30, 8:31, 9:30, 10:31, 11:31, 12:30}
m_list1 = {1:31, 2:29, 3:31, 4:30, 5:31, 6:31, 7:30, 8:31, 9:30, 10:31, 11:31, 12:30} # 윤년
def cal_leapyear(y1, y2):
    result = 0
    for i in range(y1, y2):
        if i % 4 == 0:
            if i % 400 == 0:
                result += 366
            elif i % 100 == 0:
                result += 365
            else:
                result += 366
    return result
if m1 < m2:
    D_day += cal_leapyear(y1, y2+1)
    if d1 < d2:
        for m in range(m1, m2):
            D_day += m_list[m]
        D_day += (d2 - d1 + 1)
    elif d1 > d2:
        for m in range(m1, m2):
            D_day += m_list[m]
        D_day += (d2 - d1)
elif m1 > m2:
    D_day += cal_leapyear(y1, y2)
    if d1 < d2:
        for m in range(m1, 13):
            D_day += m_list[m]
        for m in range(1, m2):
            D_day += m_list[m]
        D_day += (d2 - d1 + 1)
    elif d1 > d2:
        for m in range(m1, 13):
            D_day += m_list[m]
        for m in range(1, m2):
            D_day += m_list[m]
        D_day += 1-d1+d2

print(D_day)
