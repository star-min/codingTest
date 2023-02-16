import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
res = m
s = m
flag = 0

for i in range(1, n + 1):
    a, b = map(int, input().split())

    s += a - b

    if s < 0:
        flag = 1

    res = max(res, s)

if flag == 1:
    print(0)
else:
    print(res)