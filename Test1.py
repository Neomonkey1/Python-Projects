Python 3.11.7 (tags/v3.11.7:fa7a6f2, Dec  4 2023, 19:24:49) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
myString1 = "Making a string variable."
myString2 = "This string will have more then one line assigned to it."
myString2 = """This string will have more then one line assigned to it. Lorem lkajf;lkasjdf;lkaj,"""
print(myString2)
This string will have more then one line assigned to it. Lorem lkajf;lkasjdf;lkaj,
print(myString1)
Making a string variable.
len(myString1)
25
X = slice(0, 25, 5)
print(myString1[X])
Mgt a
txt = "       strip        "
Y = txt.strip()
print("Using the", Y, "function here.")
Using the strip function here.
myString3 = "using the upper function to make this string uppercase."
print(myString3.upper())
USING THE UPPER FUNCTION TO MAKE THIS STRING UPPERCASE.
myString4 = "Going to use the IN keyword on this string."
print("keyword" in myString4)
True
print("Array" not in myString4)
True
myString5 = "using this string to concatenate two string variables together"
print(myString1 + ' ' + myString5)
Making a string variable. using this string to concatenate two string variables together
myString6 = "Using an Escape charater \"Here\"."
print(myString6)
Using an Escape charater "Here".
num1 = 1.2
num2 = 2.1
print(num1 + num2)
3.3
num1 = 'one"
SyntaxError: unterminated string literal (detected at line 1)
num1 ='one'
print(num1 + num2)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    print(num1 + num2)
TypeError: can only concatenate str (not "float") to str
num1 = '1'
print(num1 + num2)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    print(num1 + num2)
TypeError: can only concatenate str (not "float") to str
print(int(num1) + num2)
3.1
print(10 + 10)
20
print (x += 10)
SyntaxError: invalid syntax
X = 10
X += 5
print (X)
15
Y = 5
print (X >= Y)
True
Z = 8
print (Z > 5 and Z < 10)
True
print (Y is Z)
False
print ('string' in myString1)
True
print (Y & Z)
0
print (5 & 8)
0
print (2 & 4)
0
print (2 & 3)
2
animal = ('zebra', 'alligator', 'giraffe', 'goat', 'ox')
print(animal)
('zebra', 'alligator', 'giraffe', 'goat', 'ox')
listofAnimals = list(animal)
print(listofAnimals)
['zebra', 'alligator', 'giraffe', 'goat', 'ox']
listofAnimals.append ('honey badger')
print(listofAnimals)
['zebra', 'alligator', 'giraffe', 'goat', 'ox', 'honey badger']
myString7 = 'String objects are considered tuple objects"
SyntaxError: unterminated string literal (detected at line 1)
myString7 = 'String objects are considered tuple objects'
newString1 = list(myString7)
print(newString1)
['S', 't', 'r', 'i', 'n', 'g', ' ', 'o', 'b', 'j', 'e', 'c', 't', 's', ' ', 'a', 'r', 'e', ' ', 'c', 'o', 'n', 's', 'i', 'd', 'e', 'r', 'e', 'd', ' ', 't', 'u', 'p', 'l', 'e', ' ', 'o', 'b', 'j', 'e', 'c', 't', 's']
newString1 = myString8.split(' ')
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    newString1 = myString8.split(' ')
NameError: name 'myString8' is not defined. Did you mean: 'myString1'?
newString1 = myString7.split(' ')
print(newString1)
['String', 'objects', 'are', 'considered', 'tuple', 'objects']
numList = [2,3,4,7,9]
len(numList)
5
>>> for i in numList:
...     print(i)
... 
...     
2
3
4
7
9
>>> numList[2]
4
>>> numList[0]
2
>>> numList[5]
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    numList[5]
IndexError: list index out of range
>>> numList[4]
9
>>> numList.append(11)
>>> for i in numList:
...     print(i)
... 
...     
2
3
4
7
9
11
