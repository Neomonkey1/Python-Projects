

mySentence = 'loves the color'

color_list = ['red','blue','green','teal','black','pink']
# made color_function ()
def color_function(name):
    lst = []
    for i in color_list:
        msg = '{} {} {}'.format(name,mySentence,i)
        lst.append(msg)
    return lst

# made get_name()
def get_name():
    go = True
    while go:        
        name = input ('What is your name: ')
        if name == '':
            print('You need to provide your name!')
        elif name == 'Sally':
            print('Sally, you may not use this software.') 
        else:
            go = False
    lst = color_function(name)
    for i in lst:
        print(i)


get_name()

# made and called a function
def timesTwo(x,y):
    ans = x * y
    print(ans)

timesTwo(5,9)

# using lambda
z = lambda a: a * 10
print(z(8))

# using the format()
fname = 'Holly'
lname = 'Poole'
print('Hello {} {}, welcome to Python!'.format(fname, lname) )

# using more format()
print('binary: {0:b}, decimal: {0:x}, percentage: {0:%}'.format(5))

# using a function in an variable
def getSum(num1, num2):
    answer = num1 + num2
    print('The answer is {}.'.format(answer))
getSum(2,4)
myAdd = getSum
myAdd(2,4)

# using the type()
print(type(3))
print(type('hello'))

# using input() and \ backslash
fName = input('What is your "first name"?\n>>> ')
lName = input ('What is your "last name"?\n>>> ')
print('Hello {} {}, welcome to Python!'.format(fName, lName) )

# using Data Normalization
def getName():
    fName = input('Please type in your first name without any capitalizations.\n>>> ').lower()
    print ('Thank you {}, welcome back!'.format(fName))
getName()

# using object initialization
class name:
    def __init__(self, firstName, lastName):
        #Initializing values for future objects created from this class
        self.firstName=firstName
        self.lastName=lastName
    def printName(self):
        print('Hello, I am {0} {1}'.format(self.firstName, self.lastName))

# passing in the actual object values
person=name('John', 'Smith')
person.printName()
