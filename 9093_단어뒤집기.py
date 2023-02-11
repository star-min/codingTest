import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    a = input().split()
    b = []

    for x in a:
        b.append(x[::-1])

    print(*b)