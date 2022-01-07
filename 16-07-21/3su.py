"""Write a python program to add the element of given number using function.
Example1: input = 155 -> ouptut = 11 (1 + 5 + 5)
Example2: input = 333 -> output = 9 (3 + 3 + 3)"""

def sod(n):
    if n==0:
        return 0
    else:
        return n%10+sod(n//10)
n=int(input("enter the number"))
res=sod(n)
print("sum of digits:",res)
