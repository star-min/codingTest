import sys
input = sys.stdin.readline

a = input().rstrip()
# a[::-1] = 뒤집어서 출력
if a == a[::-1]:
    print(1)
else:
    print(0)