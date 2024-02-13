#
# Author: Raymond Harrison
#
# Purpose: Encapsulation using Protected and Private methods


# Making class ProtString
class ProtString:
    def __init__(self):
        # making a protected attribute
        self._protectedVar = 'Using single underscore for protect variable'
        # making a private attribute
        self.__privateVar = 'Using double underscore for private variable'

    # making a function for private attribute    
    def getPrivate(self):
        print(self.__privateVar)

    # making a function to be able to change private attribute
    def setPrivate(self, private):
        self.__privateVar = private


# making a variable for protected attribute
obj1 = ProtString()
# making a variable for private attribute
obj2 = ProtString()











if __name__ == '__main__':
    print(obj1._protectedVar)
    #calling function to print
    obj2.getPrivate()
    #calling function to change private attribute
    obj2.setPrivate('Changing the variable of private to this.')
    #calling function to print again with new attribute
    obj2.getPrivate()
