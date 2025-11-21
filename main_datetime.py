import datetime as dt

now = dt.datetime.now()
print(now.year)
print(now.month)
print(now.weekday())

dob = dt.datetime(year=1997, month=12, day=31)
print(dob)