import webbrowser, bs4, selenium, requests, os

print(dir(webbrowser))
print(dir(bs4))
print(dir(selenium))
print(dir(requests))

# WEBBROWSER MODULE

webbrowser.open('http://www.google.com/')

# REQUESTS MODULE

print()
os.chdir(os.path.dirname(__file__))
res = requests.get('https://www.gutenberg.org/cache/epub/1112/pg1112.txt')
try:
    res.raise_for_status()
except Exception as exc:
    print('there is a problem  : %s' % (exc))
else:
    print(type(res))
    print(res.status_code == requests.codes.OK)
    print(len(res.text))
    print(res.text[:250])
    file = open('download.txt', 'wb')
    for chunk in res.iter_content(100000):
        file.write(chunk)
    file.close()

# BS4 MODULE

example = open('example.html')
soup = bs4.BeautifulSoup(example.read(), 'html.parser')
elems = soup.select('#author')
print(type(soup))
print(type(elems))
print(type(elems[0]))
print(len(elems))
print(str(elems[0]))
print(elems[0].attrs)
print(elems[0].getText())
spanElem = soup.select('span')[0]
print(str(spanElem))
print(spanElem.attrs)
print(spanElem.get('id'))

print()