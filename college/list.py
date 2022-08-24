list1 = ["ram", "sham", 10, 20]
for _ in range(len(list1)):
    print(list1[_], end=" ")
print(list1)

myList = [['cat', 'rat', 'bat'], [10, 20, 30]]
print(myList)
print(myList[0][0])
print(myList[0])

myList = ['Ram', 'sham', 'radha', 'ravan']
print(myList[1:])
print(myList[:2])
print(myList[::2])
print([10, 20, 30] + [40, 50, 60])
print([10, 20, 30] * 3)
del myList[3]
print(myList)

print('hi' in ['hi', 'hello'])
print('hi' not in ['hi', 'hello'])
color, name = ['black', 'cat']
print(color, name)

print(myList.index('sham'))
myList.append('ravan')
print(myList)
myList.insert(0, 'balram')
print(myList)
print(len(myList))
myList.remove('balram')
print(myList)
myList.sort()
print(myList)
myList.sort(reverse=True)
print(myList)
myList.sort(key=str.lower)
myList.sort(key=len)
print(myList)

# myList.count(), pop(), clear()
