import os, shelve, pprint, shutil

print()
os.chdir(os.path.dirname(__file__))
print(os.getcwd())
file = open('hello.txt', 'r')
print(file.read())
file.seek(0)
print(file.readline())
file.seek(0)
print(file.readlines())
file.close()

file2 = open('hello.txt', 'a')
file2.write('\nthis is appended')
file2.close()

# Shelve module
shel = shelve.open('sharky')
cats = ['tom', 'meaw', 'cat']
shel['cats'] = cats
shel.close()

shelf = shelve.open('sharky')
print(shelf['cats'])
shelf.close()

# pprint module
names = [{
    'fname': 'Shrinath',
    'lname': 'Korajkar'
}, {
    'fname': 'Prathamesh',
    'lname': 'Chougule'
}]
fileobj = open('mydata.py', 'w')
fileobj.write('names = ' + pprint.pformat(names) + '\n')
fileobj.close()
import mydata

print(mydata.names)

# shutil module
print(shutil.copy('hello.txt', 'hello'))
print(shutil.copy('hello.txt', 'hello2.txt'))
print(shutil.copy('hello.txt', 'hello3.txt'))
print(shutil.copy('hello.txt', 'hello4.txt'))
print(shutil.move('hello2.txt', 'hello'))
print(shutil.move('hello4.txt', 'hello/hello3.txt'))  #move and rename
print(shutil.move('hello3.txt', 'hello5.txt'))  #rename
print(shutil.copytree('hello', 'hi'))
os.unlink('hello5.txt')
os.unlink('hello/hello.txt')
os.unlink('hello/hello2.txt')
os.unlink('hello/hello3.txt')
shutil.rmtree('hi')

print()