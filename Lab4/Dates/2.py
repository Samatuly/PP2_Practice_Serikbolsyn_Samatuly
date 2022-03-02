import datetime
today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days = 1)
tomorrow = today + datetime.timedelta(days = 1)
print(yesterday.strftime("%x"))
print(today.strftime("%x"))
print(tomorrow.strftime("%x"))