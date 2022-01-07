#single inheritance
class father():#base class
    #def display(self,name,age):
    f_name="raja"
    f_age=35
class son(father):#sub class
    s_name="kumar"
    s_age=14
obj=son()
print(obj.f_name)
print(obj.s_name)
