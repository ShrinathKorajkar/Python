# TUPLES

names = ('shri', 'ram', 'radha')
print(names)
print(names[0])
print(names[1:])
print(type(('hello', )))
print(type(('hello')))

print(tuple(['cat', 'dog', 'rat']))
print(list(('cat', 'dog', 'rat')))

spam = ['hi', 'there']
cheese = spam  #referencing
cheese[0] = 'hello'
print(cheese)
print(spam)

import copy

chicken = [1, 2, 3, 4]
hen = [[1, 2], 3, 4]
dog = copy.copy(hen)
rat = copy.copy(chicken)
dog[0][0] = 0
rat[0] = 0
print(rat)
print(chicken)
print(hen)
print(dog)
hen = [[1, 2], 3, 4]
dog = copy.deepcopy(hen)
dog[0][0] = 0
print(dog)
print(hen)
