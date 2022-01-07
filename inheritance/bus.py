class userinput:
    def __init__(self,busname):
        self.busname=busname
    def display(self):
        print("vehicle name is:",self.busname)

p1=userinput(input("enter the value"))
p1.display()
