def facto(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * facto(x - 1)


def comb(n, r):
    return int(facto(n) / (facto(r) * facto(n - r)))


def solve():
    a, b = [int(x) for x in input().split()]
    print(comb(b, a))


t = int(input())
for _ in range(t):
    solve()