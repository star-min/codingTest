N = 51


def solve():
    n = int(input())
    arr = [set() for _ in range(N)]
    for _ in range(n):
        a = input()
        arr[len(a)].add(a)
    for i in range(N):
        for item in sorted(arr[i]):
            print(item)


solve()