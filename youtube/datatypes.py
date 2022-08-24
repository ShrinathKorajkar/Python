#STRINGS(immutable)

name = 'Shrinath'
para = '''hi this
is a paragraph
in multi line'''
print(name)
print(para)
print(name[0:4])
print(name[0:8:2])
print(name[:4])
print(name[4:])
print(name[::2])
print(name[::-1])
print(name[-1:0:-1])

for nam in name:
    print(nam * 2, end=' ')
print()

print(name.isalpha())
print(name.isdigit())
print(name.islower())
print(name.isupper())
print(name.lower())
print(name.upper())
name = '   shri   '
print(name.lstrip())
print(name.rstrip())

# LIST (mutable)
li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(li)

fruits = ['apple', 'orange', 'mango']
print(fruits)
fruits[1] = 'kiwi'
print(fruits[0:3:1])

li = [x**2 for x in range(10) if x % 2 == 0]
print(li)

fruits.append('orange')
print(fruits)
fruits.insert(0, 'chiku')
print(fruits)
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)
print(fruits.count('apple'))
print(fruits.index('apple'))
print(fruits.pop())
del fruits[0]
print(fruits)
fruits.clear()
print(fruits)

print(len(li))
print(max(li))
print(min(li))
print(sum(li))
print(list('hi there'))

#TOUPLES (immutable)
my_touple = (3, 4, 2, 3)
print(my_touple)
print(len(my_touple))
print(max(my_touple))
print(min(my_touple))
print(sum(my_touple))
print(tuple('hi there'))

#DICTIONARY AND SETS
myset = {1, 2, 3, 4, 4, 3, 2, 5}
print(myset)
#no indexing uniqueness
mydic = {1: 'shri', 2: 'ram', 3: 'sham', 4: 'radha'}
print(mydic)
mydic[1] = 'hari'
mydic[5] = 'maruti'
print(mydic)
for i in mydic:
    print(i, mydic[i])
