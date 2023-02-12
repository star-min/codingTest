import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    a = input().rstrip()
    b = [0] * 26

    for x in a:
        if x.islower():
            b[ord(x) - ord('a')] += 1
        elif x.isupper():
            b[ord(x) - ord('A')] += 1

    cnt = min(b)

    if cnt >= 3:
        print(f'Case {i + 1}:', 'Triple pangram!!!')
    elif cnt == 2:
        print(f'Case {i + 1}:', 'Double pangram!!')
    elif cnt == 1:
        print(f'Case {i + 1}:', 'Pangram!')
    else:
        print(f'Case {i + 1}:', 'Not a pangram')