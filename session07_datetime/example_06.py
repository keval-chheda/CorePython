from datetime import datetime
from pytz import timezone

format = "%y-%m-%d %H:%M:%S %z"

now_utc = datetime.now(timezone('utc'))
print(now_utc)
print(now_utc.strftime(format))

timezone = ['Asia/Kolkata']

for tzone in timezone :
    now_asia = now_utc.astimezone(timezone(tzone))
    print(now_asia)