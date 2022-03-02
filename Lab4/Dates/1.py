from datetime import datetime


import datetime
current = datetime.datetime.now()
five_days_ago = current - datetime.timedelta(days = 5)
print(five_days_ago)