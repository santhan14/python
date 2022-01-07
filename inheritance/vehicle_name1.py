class bus:
    def __init__(self):
        self.bus_n=input("enter the vehicle name:")
        self.ca=input("enter the value")
class bu_Vehicle(bus):
    def display(self):
        print("vehicle name is:",self.bus_n)
        print(self.ca)

obj=bu_Vehicle()
obj.display()


        
