import datetime
date1 = input('Enter a 1st date in YYYY-MM-DD format: ')
date2 = input('Enter a 2nd date in YYYY-MM-DD format: ')
year1, month1, day1 = map(int, date1.split('-'))
year2, month2, day2 = map(int, date2.split('-'))
date1 = datetime.datetime(year1, month1, day1)
date2 = datetime.datetime(year2, month2, day2)
difference = date2 - date1
print(int(difference.total_seconds()), end = " ")
print("seconds")