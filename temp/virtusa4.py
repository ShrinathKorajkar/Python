def ExtractNumber(S):
    #code here
    n = 0
    i = 0
    m = S.split()
    for i in m:
        if i.isdigit() and '9' not in i:
            n = max(n, int(i))
    if not n: return -1
    return n


inp = input()
print(ExtractNumber(inp))