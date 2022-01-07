a.)current date
import datetime
x=datetime.date.today()
y=datetime.timedelta(days=5)
print("current date before 5 days :",x-y)
#b.)yesterday,today,tomorrow
z=datetime.timedelta(days=1)
print("yesterday date is:",x-z)
print("today date is:",x)
print("tomorrow date is:",x+z)

