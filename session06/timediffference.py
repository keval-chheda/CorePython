from datetime import datetime
print ("Enter date in dd/mm/yyyy format: ") #10/10/2020
mydate = input()

myday = mydate[0:2]
mymonth = mydate[3:5]
myyear = mydate[6:10]

myday = int(myday)
mymonth = int(mymonth)
myyear = int(myyear)

now = datetime.now()
then = datetime(myyear, mymonth, myday)

time_difference = now - then
print (time_difference)