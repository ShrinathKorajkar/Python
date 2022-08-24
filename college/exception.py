def spam(divideby):
    try:
        return (40 / divideby)
    except ZeroDivisionError:
        print("cannot divide by zero")
    else:
        print("can divide no excepton")
    finally:
        print("exception handled ")


try:
    print(10 / 5)  #try block
except ZeroDivisionError:
    print("cannot divide by zero")  #exception handle
else:
    print("can divide no excepton")  #if no exception
finally:
    print("exception handled ")  #always executed

print(spam(40))
print(spam(10))
print(spam(0))

print(dir(locals()['__builtins__']))
