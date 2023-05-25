from datetime import date

today = date.today()
iso_date = date.isoformat(today)
print(iso_date)

print(date.isoformat(today))
print(type(iso_date))