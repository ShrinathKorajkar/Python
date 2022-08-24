def spam():
    global eggs
    print(eggs)
    eggs = 20


def bacon():
    print(eggs)


def ham():
    eggs = 30
    print(eggs)


eggs = 10
spam()
print(eggs)
bacon()
ham()
print(eggs)

#globals function
name = 'Phoenix'


def greet():
    globals()['name'] = 'Shri'
    name = 'Shrinath'
    print('hello ' + name)


print("global : " + name)
greet()
print("global : " + name)


def hello():
    name = 'local'
    print(globals()['name'])
    print(name)
    name = 'local2'
    globals()['name'] = 'global2'
    print(name)


name = 'global'
hello()
print(name)
