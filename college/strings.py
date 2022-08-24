print(r'this is \n in a raw string \t')
print('''this is
a multiline string''')

str1 = 'hey phoenix welcome home'
str2 = 'hello this is awesome'
print(str1[4:])
print('hey' in str1)
print(str1.upper())
print(str1.isupper())
print(str1.lower())
print(str1.islower())

print('this'.isalpha())
print('sam234e'.isalnum())
print('4589'.isdecimal())
print(' '.isspace())
print('This Is Title'.istitle())

print(str1.startswith('hey'))
print(str1.endswith('home'))
print(' '.join(['hello', 'world']))  # require list as input
print(str1.split(' '))  # return list

justify = 'hello'
print(justify.rjust(10, '*'))
print(justify.ljust(10, '*'))
print(justify.center(10, '*'))

trim = '    hello world     '
print(trim.lstrip())
print(trim.rstrip())
print(trim.strip())
spam = 'spamhello spam worldspamspam'
print(spam.strip('amsp'))


def picitems(itemdic, left, right):
    print(' PICNIC ITEMS '.center(left + right, '*'))
    for k, v in itemdic.items():
        print(k.ljust(left) + str(v).rjust(right))


picnicItems = {
    'apples': 10,
    'mango': 20,
    'cheese': 30,
    'orange': 40,
    'pepper': 50,
}
print(picnicItems)
picitems(picnicItems, 20, 5)
