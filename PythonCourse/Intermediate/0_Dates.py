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

current_time = time()

