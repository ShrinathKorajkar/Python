import re

phoneregex = re.compile(
    r'''(
    (\d{3}|\(\d{3}\))?              # area code
    (\s|-|\.)?                      # seperator
    (\d{3})                         # first 3 digits
    (\s|-|\.)                       # seperator
    (\d{4})                         # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
)''', re.VERBOSE)

emailregex = re.compile(
    r'''(
    [a-zA-Z0-9._%+-]+       # username
    @                       # @ symbol
    [a-zA-Z0-9.-]+          # domain name
    (\.[a-zA-Z]{2,4})       # dot-something
)''', re.VERBOSE)

text = input('Enter input containing emails and phone nos : ')
matches = list()

print(phoneregex.findall(text))
print(emailregex.findall(text))

for groups in phoneregex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += 'x' + groups[8]
    matches.append(phoneNum)

for groups in emailregex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    print('\n'.join(matches))
else:
    print("No phone Numbers or email address found")