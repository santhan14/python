#multiple inheritance
class father():#base class
    f_name="raja"
    f_age=40
class mother():#base class
    m_name="kumar"
    m_age=35
class son(father,mother):#sub class
    s_name="john"
    s_age=13
obj=son()
print(obj.f_age)
print(obj.m_age)
