import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

res = 0

if a < 0:
    res = d

while a < b:
    if a < 0:
        a += 1
        res += c
    else:
        a += 1
        res += e

print(res)