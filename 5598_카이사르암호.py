import sys
input = sys.stdin.readline

a = input().rstrip()
b = ''

for x in a:
##    chr(ord(x) - 3)
    c = ord(x) - 3
    if c < ord('A'):
        c += 26

    b += chr(c)

print(b)