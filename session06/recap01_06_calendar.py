import calendar
import time

current_time = time.localtime()
current_year = current_time.tm_year
current_month = current_time.tm_mon
current_day = current_time.tm_mday

weekday_name = calendar.day_name[calendar.weekday(current_year, current_month, current_day)]
month_name = calendar.month_name[current_month]

print("Current Date and Time:", weekday_name + ", " + month_name + " " + str(current_day) + ", " + str(current_year))
