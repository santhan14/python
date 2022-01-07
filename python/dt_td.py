import datetime
from datetime import timedelta
dt=datetime.date.today()
print("Today Date",dt)
td=timedelta(days=1)
dt_td=dt+td
print(dt_td)

new_year1=datetime.date(2022,1,1)
print(new_year1)
new_year=(dt-new_year1)

print("New Year",new_year)
