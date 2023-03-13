import math


def solve():
    a = int(input())
    n = math.ceil(math.log2(a))
    x = 2 ** n - a
    print(2 ** n - 2 * x)


solve()