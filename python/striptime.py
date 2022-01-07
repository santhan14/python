from datetime import datetime

dt_string = "12/11/2018 09:15:32"

print("Strptime")

# Considering date is in dd/mm/yyyy format
dt_object1 = datetime.strptime(dt_string, "%d/%m/%Y %H:%M:%S")
print("dt_object1 =", dt_object1)

# Considering date is in mm/dd/yyyy format
dt_object2 = datetime.strptime(dt_string, "%m/%d/%Y %H:%M:%S")
print("dt_object2 =", dt_object2)

print("=======================================================")

print("Strftime")

now = datetime.now() # current date and time

year = now.strftime("%Y")
print("year:", year)

month = now.strftime("%m")
print("month:", month)

day = now.strftime("%d")
print("day:", day)

time = now.strftime("%H:%M:%S")
print("time:", time)

date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
print("date and time:",date_time)	
print("=======================================================")

a="17/11/2021"
print(a)
b=datetime.strptime(a, "%d/%m/%Y")
print(b)
print("=======================================================")

from datetime import datetime, date



t1 =date(year = 2018, month = 7, day = 12)
t2 =date(year = 2017, month = 12, day = 12)
t3 = t1 - t2
print("t3 =", t3)
print("========================================================")

print("timedelta")

import datetime

t1 = datetime.timedelta(weeks = 2, days = 5, hours = 1, seconds = 33)
t2 = datetime.timedelta(days = 4, hours = 11, minutes = 4, seconds = 54)
t3 = t1 - t2

print("t3 =", t3)
print("========================================================")
print("New Year")
now_date=datetime.datetime.today()
print(now_date)
new_year1=datetime.date(2022,1,1)





