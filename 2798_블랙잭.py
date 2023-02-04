import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
res = 0

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            if res < a[i] + a[j] + a[k] <= m:
                res = a[i] + a[j] + a[k]

print(res)