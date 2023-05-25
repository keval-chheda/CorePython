import datetime

# current date
today = datetime.date.today()
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)
print("Weekday (Mon=0, Sun=6):", today.weekday())
print("ISO Weekday (Mon=1, Sun=7):", today.isoweekday())
print("ISO Format:", today.isoformat())

# current datetime
now = datetime.datetime.now()
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)
print("Microsecond:", now.microsecond)
print("Weekday (Mon=0, Sun=6):", now.weekday())
print("ISO Weekday (Mon=1, Sun=7):", now.isoweekday())
print("ISO Format:", now.isoformat())
