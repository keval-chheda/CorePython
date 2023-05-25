#timedelta is used for calculate difference between dates and data manipulation

from datetime import datetime, timedelta

curr_date = datetime.now()
print("initial date", curr_date)

future_date = curr_date + timedelta(days= 365)
print("future date will be after 1 year", future_date)



