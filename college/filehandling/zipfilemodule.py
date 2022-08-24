import zipfile, os

os.chdir(os.path.dirname(__file__))
file = zipfile.ZipFile('new.zip', 'w')
file.write('hello.txt', compress_type=zipfile.ZIP_DEFLATED)
file.close()

file2 = zipfile.ZipFile('new.zip', 'r')
print(file2.namelist())
spam = file2.getinfo('hello.txt')
print(spam.file_size)
print(spam.compress_size)
file2.extractall()
file2.extract('hello.txt')
file2.extract('hello.txt', '.')
file2.close()
