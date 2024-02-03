# no arrays in Python but lists work basically the same
# Using a list
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

# using a tuple
tupleList = ('ray', 'brandi', 'luke')
print(tupleList)
for i in tupleList:
    print(i)
a = tupleList.count('luke')
print(a)

# using a set
mySet = {'football', 'baseball', 'hockey'}
print(mySet)
mySet.add('basketball')
print(mySet)
mySet.remove('baseball')
print(mySet)
mySet2 = {'football', 'tennis', 'hockey'}
z = mySet.difference(mySet2)
print(z)

# using loop on list
for x in myList:
    print (x)

# using the count()
y = myList.count('eggs')
print(y)

# using the sort()
myList.sort()
print(myList)
