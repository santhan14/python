
#List Argument Function

def total(marks):
    return sum(marks)
print(total([55,55,90]))


#Recursive Mathod
def factorial(x):
    if x==1:
        return 1
    else:
        return(x*factorial(x-1))
print("factorial:",factorial(1))

#DateTime

import datetime as dt
time=dt.datetime.now()
print(time)
current_time=dt.time(3,15,14,34556)
print(current_time)
current=dt.datetime.now()
new_year=dt.datetime(2022,1,1)
difference=new_year-current
print(difference)
