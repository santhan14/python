obj=open("sto.txt","r")
print(obj.read(10))
print(obj.read(10))

with open("sto.txt","r")as sto:
    obj1=sto.read(20)
    print(obj1)
    obj1.seek(2)
        
    
