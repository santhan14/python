#get input from user
import re
mn=input("enter the mobile number")
if len(mn)==10:
    valid=re.search("[0-9]{10}",mn)
    print("result:",valid)
elif len(mn)<10:
    print("your input is less then mobile number")
elif len(mn)>10:
    print("your input is greater then mobile number")
#else:
   # print("this is string so only give 10 digital numbers")

