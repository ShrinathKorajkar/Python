def isp(r):
    found = False
    for a in range(len(r) - 1):
        b = a + 1
        if r[b][0] <= r[a][1]:
            found = True
            break
    if found:
        return (a, b)
    return False


c, n, k = list(map(int, input().split()))
r = []
for i in range(n):
    r.append(list(map(int, input().split())))
r.sort()
init = isp(r)
if not init:
    print("Good\n")
elif k == 0:
    print("Bad\n")
else:
    pos = False
    for i in init:
        o = r[:i] + r[i + 1:]
        cur = isp(o)
        if cur:
            continue
        big = max(o[0][0] - 1, c - o[-1][1])
        for k in range(1, n - 1):
            d = o[k][0] - o[k - 1][1] - 1
            if d >= r[i][1] - r[i][0] + 1:
                big = d
                break
        if big >= r[i][1] - r[i][0] + 1:
            pos = True
            break

    if pos:
        print("Good\n")
    else:
        print("Bad\n")
