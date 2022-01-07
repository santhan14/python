#Before write this content
file=open("test.txt","r")
print(file.read())

file=open("test.txt","w")
file.write("i write this content")
file.close()

file=open("test.text","a")
file.write("successfully append this one")
file.close()

file=open("test.text","r")
print(file.read())


#After write this content


