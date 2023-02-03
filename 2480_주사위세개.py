import sys
input = sys.stdin.readline

a = list(map(int, input().split()))

''' sort()를 사용하지 않았을 경우
if a[0] == a[1] == a[2]:
    print(10000 + a[0] * 1000)
elif a[0] == a[1]:
    print(1000 + a[0] * 100)
elif a[1] == a[2]:
    print(1000 + a[1] * 100)
elif a[2] == a[0]:
    print(1000 + a[2] * 100)
else:
    print(max(a) * 100) # 'max()' 리스트 내 가장 큰수를 찾음
'''
a.sort()  # 'sort()' = 작은값 부터 정렬
if a[0] == a[2]:
    print(10000 + a[0] * 1000)
elif a[0] == a[1] or a[1] == a[2]:
    print(1000 + a[1] * 100)
else:
    print(max(a) * 100) # 'max()' 리스트 내 가장 큰수를 찾음