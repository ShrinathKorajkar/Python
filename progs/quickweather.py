import json, requests, pprint, os
from datetime import datetime

os.chdir(os.path.dirname(__file__))
url2 = 'http://api.openweathermap.org/data/2.5/weather?lat=15.852792&lon=74.498703&appid=5a36056e843b5e2b81767ba9c20a8584'
response = requests.get(url2)
response.raise_for_status()
weatherdata = json.loads(response.text)
# pprint.pprint(weatherdata)
file = open('wdata.txt', 'w')
file.write(pprint.pformat(weatherdata))

w = weatherdata
today = datetime.fromtimestamp(w['dt'])
sunrise = datetime.fromtimestamp(w['sys']['sunrise'])
sunset = datetime.fromtimestamp(w['sys']['sunset'])
print('\nCurrent weather in %s : ' % (w['name']))
print('\nDate : ', today)
print('sunrise : ', sunrise)
print('sunset : ', sunset)
print('Description : ', w['weather'][0]['description'])
print('max Temperature : ', w['main']['temp_max'], 'k')
print('min Temperature : ', w['main']['temp_min'], 'k')
print('Temperature : ', w['main']['temp'], 'k')
print('Humidity : ', w['main']['humidity'], '%\n')

# location = input('Enter location : ')
# url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3' % (location)

# w = weatherdata['list']
# print('Current weather in %s : ' % ('Belgaum'))
# print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'], '\n')
# print('Tommorow : ')
# print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'], '\n')
# print('Day after Tommorow')
# print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'], '\n')
