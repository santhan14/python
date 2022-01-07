class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
        print("Hello my name is " + self.name)
        
name=input("Enter Your Name Plese")
age=int(input("Enter Your Age Please"))

p1 = Person(name,age)
p1.myfunc()
