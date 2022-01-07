lst = []
ele = int(input("Enter number of elements : "))
for j in range(0, ele):
	el =input("enter the element")
	lst.append(el)
print("current list:",lst)
n =int(input("enter the rotation number:"))
lst=(lst[-n:] + lst[:-n])
print("after rotate:",lst)
  


