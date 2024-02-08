
# creating class
class Person:
    # creating a dunder method to attach the arguments for creating the class object
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

# creating inheritance
class Student(Person):
    GPA = 3.0
    studying = ""

#creating another inheritance
class Teacher(Person):
    teaches = ""
    yearsEmp = 10

# adding class object 
add_person = Person('John', 'Smith')

print(add_person.fname)



