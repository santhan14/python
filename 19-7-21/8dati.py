#a.)current datetime
import datetime
x=datetime.datetime.now()
print("current date and time:",x)
#b.)current year
print("current year:",x.strftime("%y"))
#c.)month of year
print("month of year:",x.strftime("%m"))
#d.)week number of the year
print("week number of the year:",x.strftime("%U"))
#e.)week day of the week
print("week day of the week:",x.strftime("%w"))
#f.)day of year
print("day of year:",x.strftime("%j"))
#g.)day of the month
print("day of month:",x.strftime("%d"))
#h.)day of week
print("day of week:",x.strftime("%w"))
#i.)weekday name
print("weekday name:",x.strftime("%A"))
#j.)microseconds
print("microsec:",x.strftime("%f"))

