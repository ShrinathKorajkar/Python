name = 'ram'
while name == input('enter name : '):
    print('Hi ram')
    age = 18
    while age == int(input('enter age : ')):
        print('mature')
        break
    break
print('Thank You')

print('numbers 0-5')
for x in range(0, 6):
    print(x)

print('numbers 5-0')
for x in range(5, -1, -1):
    print(x)

print('numbers 0-10 even')
for x in range(0, 11, 2):
    print(x)

for x in range(10):
    if x // 3 == 0:
        pass
    if x // 3 == 1:
        continue

print('random nos')
import random, sys
for i in range(5):
    print(random.randint(1, 10))  # including both end points
    sys.exit()