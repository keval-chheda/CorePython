from datetime import datetime
print("Enter the date in format dd/mm/yyyy")
mydate = input()

myday = int(mydate[0:2])
mymonth = int(mydate[3:5])
myyear = int(mydate[6:10])

# myday = int(myday)
# mymonth = int(mymonth)
# myyear = int(myyear)

now = datetime.now()
custom = datetime(myyear, mymonth, myday)

time_diff = now - custom
print(time_diff)
