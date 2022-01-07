a=(1,2.5,False,"francis")
print(a)
print(type(a))
print(type(a[2]))
print(a[-1])
b=list(a)
print(type(b))
for i in a:
    print(i)

del a
try:
    print(a)
except Exception as ex:
    print(ex)

a_=(1,2,3,4,5)
b_=(5,6,7,8,9)
ab=a_+b_
print(ab)
print(ab.count(5))
c=(a_,b_)
print(c)
print(c[1][0])
x=("john",)*5
print(x)
print(min(a_))
print(max(a_))

