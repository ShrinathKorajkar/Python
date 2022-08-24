import requests, sys, webbrowser, bs4

print('Loading.....')
res = requests.get('https://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
linkElems = soup.select('a')
print(linkElems)
numOpen = min(len(linkElems), 5)
for i in range(numOpen):
    webbrowser.open('https://google.com' + linkElems[i].get('href'))