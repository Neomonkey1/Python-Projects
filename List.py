myList = ['milk', 'eggs', 'bacon']
for x in myList:
    print(x)
myList.append('bagel')
print(myList)
copyList = myList.copy()
print(copyList)
myList2 = [1, 2, 3, 4]
myList3 = myList + myList2
print(myList3)
copyList.remove('bagel')
print(copyList)
copyList.reverse()
print(copyList)

tupleList = ('ray', 'brandi', 'luke')
print(tupleList)
for i in tupleList:
    print(i)
a = tupleList.count('luke')
print(a)

mySet = {'football', 'baseball', 'hockey'}
print(mySet)
mySet.add('basketball')
print(mySet)
mySet.remove('baseball')
print(mySet)
mySet2 = {'football', 'tennis', 'hockey'}
z = mySet.difference(mySet2)
print(z)
