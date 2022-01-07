#1
list=[10,20,30,40]
list1=[300,400,500]
list2=[5000,6000]
list3=7000
list.insert(2,list1)
list1.insert(2,list2)
list2.insert(2,list3)
print(list)

list1 = [10, 20, [300, 400, [5000,6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)



#2
a=["a","b","m","n"]
a1=["c","l"]
a2=["d","e","k"]
a3=["f","g"]
a.insert(2,a1)
a1.insert(1,a2)
a2.insert(2,a3)
a3.insert(2,'h')
a3.insert(3,'i')
a3.insert(4,'j')
print(a)

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
subList = ["h", "i", "j"]
list1[2][1][2].extend(subList)
print(list1)

#3
b=["Hello ", "take "]
b1=["Dear", "sir"]
b2=[x+y for x in b for y in b1]
print(b2)

#4
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict1.update(dict2)
print(dict1)

#5
sampleDict = {'a': 100, 'b': 200, 'c': 300}
print(200 in sampleDict.values())

#6
sampleDict = {
     'emp1': {'name': 'Jhon', 'salary': 7500},
     'emp2': {'name': 'Emma', 'salary': 8000},
     'emp3': {'name': 'Brad', 'salary': 6500}
}
sampleDict['emp3']['salary'] = 8500
print(sampleDict)

#7
sampleSet = {"Yellow", "Orange", "Black"}
sampleList = ["Blue", "Green", "Red"]
set=sampleSet.update(sampleList)
print(sampleSet)

#8
tuple1 = (11, 22)
tuple2 = (99, 88)
print('tuple1=:',tuple2,'tuple2=:',tuple1)

#9
tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0]=222
print(tuple1)
