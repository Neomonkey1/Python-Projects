# for and while loops

# for loops
i = 0
for i in range(10):
    print('{} iteration through the loop.'.format(i))
    i += 1

# while loops go till condition met
i = 0
while i < 10:
    print('{} iteration through the loop.'.format(i))
    i += 1

# using break statement
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# using continue statement
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
    
# using an else statement
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print('i is no longer less than 6')

# using range() in for loop
for X in range(6):
    print(X)

# using for loop in list
fruits = ['apple', 'banana', 'cherry']
for x in fruits:
    print(x)
# using the enumerate ()
name = 'Python'
print(len(name))
for i in enumerate(name):
    print(i)
