from datetime import datetime,timedelta
current=datetime.now()
new=current-timedelta(day=52)
print(new)
