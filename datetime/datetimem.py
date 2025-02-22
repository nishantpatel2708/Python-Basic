import datetime

dt = datetime.datetime(year=2023, month=2, day=11)
dt1 = datetime.datetime(year=2023, month=2, day=12, hour=15, minute=55)
print(dt)
print(dt1)

ct = datetime.datetime.today()
print(ct)
# print(ct.day, ct.month, ct.year)

yesterday = ct - datetime.timedelta(days=1)
print(yesterday)