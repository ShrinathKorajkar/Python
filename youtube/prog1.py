print('hello world')
print('hi my name is Shri')

# DATA TYPES
print(2, '\t\t', type(2))
print('hello', '\t\t', type('hello'))
print(2.3, '\t\t', type(2 / 3))
print((5 + 3j), '\t\t', type((5 + 3j)))
print(['ram', 'sham'], type(['ram', 'sham']))
print(True, '\t\t', type(True))
print(None, '\t\t', type(None))

name = input('enter name : ')
age = int(input('Enter age : '))
dob = input('Enter dob : ')
user = bool(input('new user ? : '))
food = list(input('Enter foods :'))
print(name, age, dob, user, food, sep=" ")

# #OPERATORS
a = 5
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a // b)
print(a**b)

a = int(input('enter no 1 : '))
b = int(input('enter no 2 : '))
c = int(input('enter no 3 : '))
print('average : ', ((a + b + c) / 3))

# LOOPS
a = range(10)
print(a)
a = list(range(10))
print(a)

for i in range(10):
    print(i, end=' ')
print()

a = ['ram', 'sham', 'radha']
for name in a:
    print(name * 2, end=' ')

while True:
    print('hello')
    break  # break using ctrl+c


# #FUNCTIONS
def greet(name, food='tea'):
    print('hello', name)
    print('have', food)


greet('shri')
greet('ram', 'pasta')


def hello(names):
    for name in names:
        print('hello', name)


names = ['shri', 'ram', 'sham']
hello(names)
