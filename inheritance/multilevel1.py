#multilevel inheritance
class gfather():#base class
    gf_name="raja"
    gf_age=70
class father(gfather):#inermediate class
    f_name="kumar"
    f_age=35
class son(father):#sub class
    s_name="john"
    s_age=13
obj=son()
print(obj.f_age)
print(obj.s_age)
