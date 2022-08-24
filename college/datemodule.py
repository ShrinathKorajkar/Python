from datetime import datetime, date, time

# Date
print()
today = date.today()
dob = date(2001, 6, 23)
date_to_str = date.isoformat(dob)
str_to_date = date.fromisoformat(date_to_str)
print("today : ", today)
print('year :', today.year, ' month :', today.month, ' day :', today.day)
print("dob : ", dob)
print('date to str : ', date_to_str)
print('str to date : ', str_to_date)
age = today - dob
print(age)
print('age : ', age.days // 365, 'years, ', (age.days % 365) // 30, 'months, ',
      (age.days % 365) % 30, 'days')
days = [
    'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday',
    'sunday'
]
print('day : ', days[today.weekday()])
print()

# Time
tim = time()
mytime = time(11, 23, 32)
print('nowtime :', tim)
print('mytime :', mytime)
print('mytime :', mytime.hour, mytime.minute, mytime.second)
print()

# Date Time
tod = datetime.today()  # dont have timezone
now = datetime.now()  #  have timezone
timedate = datetime(2022, 2, 4, 11, 23, 32)
print("today : ", tod)
print("my date time : ", timedate)
print("now : ", now)
print(now - timedate)
print(datetime.combine(today, tim))
print()

# strptime, strftime
print('without format :', now)
s = now.strftime('%d/%m/%Y %H:%M:%S')
print('with format 1 :', s)
s = now.strftime('%A %m %y')
print('with format 2 :', s)
s = now.strftime('%I %p %S')
print('with format 3 :', s)
mydate = '07/02/2022'
format = '%d/%m/%Y'
print(datetime.strptime(mydate, format))  # return date object
print()

# datetime and time contains all methods of date
# other func replace(), utcnow()