var=open("re.txt","a")
var.write("welcom to append")
var.close()
try:
    f=open("1stay.txt","r")
    print(f.read())
except Exception as error:
    print(error)






