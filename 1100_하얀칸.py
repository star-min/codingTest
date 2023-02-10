import sys
input = sys.stdin.readline

a = []

for i in range(8):
    b = input().rstrip()
    a.append(b)

res = 0

for i in range(8):
    for j in range(8):
        if a[i][j] == '.':
            continue

        if (i % 2 == 0 and j % 2 == 0) or \
            (i % 2 == 1 and j % 2 == 1):
            res += 1
print(res)