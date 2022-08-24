import os

# print(dir(os))

print("\nos.getcwd : ", os.getcwd())
print("os.listdir : ", os.listdir('D:\\visual studio\\Python\\'))
os.chdir('D:\\visual studio')
os.makedirs('D:/visual studio/Python/college/oscreateddir')
os.rmdir('D:/visual studio/Python/college/oscreateddir')

# os.path Module
path = "D:\\visual studio\\Python\\progs\\Typosedata.txt"

print("os.path.join : ", os.path.join('C:', 'users', 'shrin'))
print("os.path.abspath : ", os.path.abspath('.'))
print("os.path.isabs : ", os.path.isabs('.'))
print("os.path.isabs : ", os.path.isabs(os.path.abspath('.')))
print("os.path.relpath : ", os.path.relpath('.', 'D:\\shrin'))
print("os.path.split : ", os.path.split(path))
print("os.path.dirname : ", os.path.dirname(path))
print("os.path.basename : ", os.path.basename(path))
print("os.path.getsize : ", os.path.getsize(path))
print("os.path.exists : ", os.path.exists(path))
print("os.path.isdir : ", os.path.isdir(path))
print("os.path.isfile : ", os.path.isfile(path))
print(path.split(os.path.sep))

# os.walk
print()
for folder, subfolders, files in os.walk(
        os.path.dirname(__file__) + '\\filehandling'):
    print('Current folder is : ' + folder)
    for subfolder in subfolders:
        print('Subfolder of %s : %s' % (folder, subfolder))
    for file in files:
        print(f'File in {folder} : {file}')
    print()

print()