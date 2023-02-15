import sys
input = sys.stdin.readline

a = int(input())
n = 1

while a > 1:
    if a % 2 == 0:
        a //= 2
    else:
        a = 3 * a + 1

    n += 1

print(n)