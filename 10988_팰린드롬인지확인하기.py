import sys
input = sys.stdin.readline

a = input().rstrip()
# a[::-1] = 뒤집어서 출력 콜론 마다 시작과 끝 을 삽입할수 있으나 비어있으면 전부 뒤집는다.
if a == a[::-1]:
    print(1)
else:
    print(0)