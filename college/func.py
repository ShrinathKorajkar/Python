def hello():
    print('hello ram')


if __name__ == '__main__':
    print('hello')

hello()
hello()

eggs = 10


def display():
    eggs = 20
    print(eggs)


display()
print(eggs)


def mul(a, b):
    return a + b


# LAMBDA equillant
mul = lambda a, b: a + b

print(mul(3, 5))


def nonKey(*args):
    for i in args:
        print(i)


def Key(**kwargs):
    for i, j in kwargs.items():
        print(i, j)


nonKey(1, 2, 3, 4)
Key(sunday=1, monday=2)
