import sys
input = sys.stdin.readline

n, x = map(int, input().split())
a = list(map(int, input().split()))
b = []
for y in a:
    if y < x:
        b.append(y)
print(*b)
