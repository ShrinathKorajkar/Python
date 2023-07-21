def NthTerm(N):
    if N == 1:
        return 2
    if N == 2:
        return 2

    smallerOut = NthTerm(N - 2)
    if N % 2 == 0:
        return smallerOut**3
    else:
        return smallerOut**2


n = int(input())
print(NthTerm(n))
