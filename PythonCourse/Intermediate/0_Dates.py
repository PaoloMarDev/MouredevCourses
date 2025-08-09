### Dates ###

from datetime import datetime 
from datetime import time 

def PrintDate(date):
    print(date)
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())

now = datetime.now()


PrintDate(now)

year_2026 = datetime(2026, 1, 1)

print(year_2026)

current_time = time(21, 6, 0)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

from datetime import date

current_date = date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(2025, 10, 6)

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(current_date.year, current_date.month + 1, current_date.day)

print(current_date.month)


diff = year_2026 - now
print(diff)

diff = year_2026.date() - current_date
print(diff)

print(year_2026.time())

from datetime import timedelta

start_timedelta = timedelta(200, 10, 100, weeks=10)
end_timedelta = timedelta(300, 100, 100, weeks=13)


print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)
print(end_timedelta / start_timedelta)




