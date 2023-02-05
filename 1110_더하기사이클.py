import sys
input = sys.stdin.readline

n = int(input())
cnt = 0

a = n

while True:
    b = a // 10 + a % 10
    a = (a % 10) * 10 + b % 10
    cnt += 1

    if a == n:
        break

print(cnt)