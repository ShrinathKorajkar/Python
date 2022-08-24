import re

sentence = input('\nenter sentence : ')
regex = re.compile(
    r'''
    ((\d{2}|\d{4})      #day or year
    (/|-)               #seperator
    \d{2}               #month
    (/|-)               #seperator
    (\d{4}|\d{2}))      #year or day
    ''', re.VERBOSE)
mo = regex.findall(sentence)
if mo == []:
    print('there are no dates present in the sentence \n')
else:
    print('Dates in the given sentence are : ')
    for date in mo:
        print(date[0])
    print()