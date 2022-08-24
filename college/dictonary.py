myDic = {'name': 'shri', 'age': 20}
dicComprehension = {val: k for k, val in myDic.items()}

print(myDic)
print(dicComprehension)
print(myDic['name'])
print({'hi', 'hello'} == {'hello', 'hi'})

print(myDic.values())
print(myDic.keys())
print(myDic.items())
for k in myDic.keys():
    print(k)
for v in myDic.values():
    print(v)
for vk in myDic.items():
    print(vk)
for v, k in myDic.items():
    print('v : ', v, ' k : ', k)

print(myDic.get('name', 'no name'))
print(myDic.get('na', 'no name'))

print(myDic.setdefault('hi', 'hello'))
print(myDic.setdefault('name', 'hello'))

# merging dict
myDic2 = {'a': 1, 'b': 2}
myDic.update(myDic2)
print(myDic)

msg = 'hello good morning'
count = {}
for character in msg:
    count.setdefault(character, 0)
    count[character] += 1
print(count)

# PRITTY PRINTING
import pprint

pprint.pprint(count)

# SETS
mySet = {1, 2, 3}
mySet = set([1, 2, 3])
print(mySet)
mySet.add(4)
mySet.update([5, 6, 7])
mySet.remove(7)  # raise error
mySet.discard(8)  # dont raise error
print("Set 1 : ", mySet)

mySet2 = {1, 4, 6, 9}
print("Set 2 : ", mySet2)
print(mySet | mySet2)  # union
print(mySet & mySet2)  # intersection
print(mySet - mySet2)  # difference
print(mySet ^ mySet2
      )  # symmetric difference (not common to both -> union - intersection)
