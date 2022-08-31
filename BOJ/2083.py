import sys

a,b,c = sys.stdin.readline().split()

if int(b) > 17 or int(c) >= 80:
    print(a,'Senior')
else:
    print(a,'Junior')