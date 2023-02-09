import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    a = input().rstrip()
    res = 0
    v = 0

    for x in a:
        if x == '0':
            v += 1
        else:
            v = 0
        res += v

    print(res)