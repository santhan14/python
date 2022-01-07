"""Write a recursive function to calculate the sum of numbers from 0 to 10
Expected Output: 55"""

n=int(input("enter the value"))
s=0
for i in range(1,n+1):
    s=s+i
print("sum of value is:",s)
