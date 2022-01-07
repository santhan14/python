f=open("new.txt","w")
f.write("Hii this is new line")
f.close()
f=open("new.txt","r")
print(f.read())

