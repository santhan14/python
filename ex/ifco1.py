class A:
    def add(self,a=None,b=None):
        if a!=None and b!=None:
            print(a+b)
        else:
            print(a)

obj=A()            
obj.add()
