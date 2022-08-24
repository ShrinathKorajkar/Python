def spam():
    global eggs
    eggs = 20
    print(eggs)


def bacon():
    eggs = 30
    print(eggs)


def ham():
    eggs = 40
    print(eggs)


eggs = 10
spam()
bacon()
ham()
print(eggs)


def spam():
    try:
        print(eggs)
    except ZeroDivisionError:
        print('hi error')


eggs = 'global'
spam()