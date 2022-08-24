import re

# print(dir(re))

regex = re.compile(r'hello')
mo = regex.search('hello there hello')
if mo != None:
    print(mo.group())
    print(mo.groups())
    print(mo.groupdict())
    print(mo.span())
    print(mo.end())
mo = regex.match('hello my name is hello')
if mo != None:
    print(mo.group())
mo = regex.fullmatch('hello')
if mo != None:
    print(mo.group())
mo = regex.findall('hello my name is hello')
if mo != None:
    print(mo)
mo = regex.sub('hey', 'hello my name is hello')
if mo != None:
    print(mo)
mo = regex.finditer('hello my name is hello')
if mo != None:
    print(mo)
mo = regex.split('hello my name is hello')
if mo != None:
    print(mo)
mo = regex.subn('hi', 'hello my name is hello')
if mo != None:
    print(mo)

regex = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
mo = regex.search('hello my phone number is : 415-576-3322, : 415-234-4948')
if mo != None:
    print(mo.group())
    print(mo.group(1))
    print(mo.group(2))
    print(mo.groups())

regex = re.compile(r'batman\? |spiderman\?')
mo = regex.search('i love spiderman?')
if mo != None:
    print(mo.group())

regex = re.compile(r'bat(wo)?man')
mo = regex.search('i love batman more than batwoman')
if mo != None:
    print(mo.group())

regex = re.compile(r'bat(wo)*man')
mo = regex.search('i am not batwowoman i am batman')
if mo != None:
    print(mo.group())

regex = re.compile(r'bat(wo)+man')
mo = regex.search('i am batman not batwoman')
if mo != None:
    print(mo.group())

regex = re.compile(r'(ha){3}')
mo = regex.search('hahahahaha')
if mo != None:
    print(mo.group())
regex = re.compile(r'(ha){3,}')
mo = regex.search('hahahahahaha')
if mo != None:
    print(mo.group())
regex = re.compile(r'(ha){,5}')
mo = regex.search('hahahahahaha')
if mo != None:
    print(mo.group())
regex = re.compile(r'(ha){3,5}')
mo = regex.search('hahahahahaha')
if mo != None:
    print(mo.group())
regex = re.compile(r'(ha){3,5}?')
mo = regex.search('hahahahahaha')
if mo != None:
    print(mo.group())

regex = re.compile(r'\d+\s\w+')
mo = regex.findall('12 dams, 3 rivers, 1 country')
if mo != None:
    print(mo)

regex = re.compile(r'[aeiouAEIOU]')
mo = regex.findall('My name is Anthony Gonsalves')
if mo != None:
    print(mo)

regex = re.compile(r'[^aeiouAEIOU]')
mo = regex.findall('My name is Anthony Gonsalves')
if mo != None:
    print(mo)

regex = re.compile(r'^hello')
mo = regex.findall('hello My name is Anthony Gonsalves')
if mo != None:
    print(mo)

regex = re.compile(r'Gonsalves$')
mo = regex.findall('hello My name is Anthony Gonsalves')
if mo != None:
    print(mo)

regex = re.compile(r'^hello.*Gonsalves$')
mo = regex.findall('hello My name is Anthony Gonsalves')
if mo != None:
    print(mo)

regex = re.compile(r'.at')
mo = regex.findall('the cat in the hat sat at the fat')
if mo != None:
    print(mo)

regex = re.compile(r'firstname : (.*) lastname : (.*)')
mo = regex.search('firstname : shri lastname : koraj')
if mo != None:
    print(mo.group())

regex = re.compile(r'<.*?>')
mo = regex.search('<to serve man> for dinner>')
if mo != None:
    print(mo.group())

regex = re.compile(r'.*', re.DOTALL)
mo = regex.search('serve the public \nserve the society')
if mo != None:
    print(mo.group())

regex = re.compile(r'robosoft', re.I)
mo = regex.search('Robosoft if fake')
if mo != None:
    print(mo.group())

regex = re.compile(r'agent \w+')
mo = regex.sub('cencored', 'agent vinod is bullshit')
if mo != None:
    print(mo)

regex = re.compile(r'agent (\w)(\w)+')
mo = regex.sub(r'\1***', 'agent alice is giving secret to agent bob')
if mo != None:
    print(mo)

regex = re.compile(
    r'''((\d{3}|\(\d{3}\))?
        (\s|-|\.)?
        \d{3}
        (\s|-|\.)?
        \d{4}
        )''', re.VERBOSE)

print(regex.findall('413-230-3244 is 123.245.1247 456 765 7644 hey 234 2344'))
