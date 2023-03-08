def solve():
    s = input()
    s = s.upper()
    hist = {}
    for c in s:
        if c in hist.keys():
            hist[c] += 1
        else:
            hist[c] = 1
    big = 0
    for key in hist.keys():
        big = max(big, hist[key])
    cnt = 0
    for key in hist.keys():
        if hist[key] == big:
            cnt += 1
            rst = key
    if cnt != 1:
        print("?")
    else:
        print(rst)


solve()