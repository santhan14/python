import datetime
now=datetime.date.today()
print("Today date",now)
new_year1=datetime.timedelta(days=365)
print(new_year1)
new_year=new_year1-now

print("New Year",new_year)
print(type(new_year))

