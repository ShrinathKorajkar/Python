def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


mylist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
st = 'hello world'
tup = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
print(histogram(mylist))
print(histogram(st))
print(histogram(tup))
