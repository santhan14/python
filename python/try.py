try:
    a=["John","Denif","Red","Vela"]
    print(a[5])
except Exception as ex:
    print(ex)
    

b=(dir(locals()['__builtins__']))
print(len(b))
