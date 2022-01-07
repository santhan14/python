#2.Write a Python function that takes a list and returns a new list with unique elements of the first list.
#Sample List : [1,2,3,3,3,3,4,5]
#out put
#Unique List : [1, 2, 3, 4, 5]
def fun():
    n=[1,2,3,3,3,4,5]
    x=list(dict.fromkeys(n))
    return x
print(fun())
