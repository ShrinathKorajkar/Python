# print('Hello world')
# name = input('enter name : ')
# print("my name : " + name + ' length : ' + str(len(name)))
# age = int(input('enter age : '))
# print("my age : " + str(age))
print(4 == 4 and 4 == 4.0)
print(4 == 4 and not 4 == ' 4 ')
if 4 == 4.0:
    print(True)
elif 4 == 4:
    print(True)
else:
    print(False)

sum = range(10)
print('sum is : ', sum[-1])
print('sum is : ', sum[0])
print('sum is : ', sum.start)
print('sum is : ', sum.stop)

print("ram", "sham", "shri", sep="@")
print("ram", "sham", "shri")
print("ram" + "sham" + "shri")
print("ram" + "sham" + "shri", end=' ')

print("this is " + \
    "multiline print")      # line continuation operator

name = 'Phoenix'
age = 21
print("my name is %s . i am %s years old" % (name, age))
print(f"my name is {name} . i am {age} years old")
print("hello {} . your age is {}".format(name, age))

print(ord('A'), ord('Z'), ord('a'), ord('z'), ord('0'), ord('9'))

print("hello" if True else "goodbye")  # ternary operator

# datatypes -> Integer, String, Boolean, Float
''' DocString Comment '''
