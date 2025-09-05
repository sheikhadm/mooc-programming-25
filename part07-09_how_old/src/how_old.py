# Write your solution here
from datetime import datetime, timedelta
day = int(input('Day: '))
month = int(input('month: '))
year = int(input('year: '))

dob = datetime(year,month,day)
mil = datetime(1999,12,31)
dif = mil - dob

if dif.days > 0 :
    print(f'You were {dif.days} days old on the eve of the new millennium.')
elif dif.days < 0:
    print('You weren\'t born yet on the eve of the new millennium.')