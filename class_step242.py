

# Creating a class

class Computer:
    #creating a dunder method to attach the arguments for creating the class object
    def __init__(self, brand, cpu, os, disk_space, ram):
        self.brand = brand
        self.cpu = cpu
        self.os = os
        self.disk_space = disk_space
        self.ram = ram

#adding arguments to make object
comp = Computer('Dell', 'Intel Core i7', 'Windows 11', '1 TB', '16 GB')

#adding a method
def myFunc(self):
    print('This Computer is a {} with an {} inside using {} with a {} hard drive and {} RAM'.format(self.brand,self.cpu,self.os,self.disk_space,self.ram))




if __name__ == '__main__':
    myFunc(comp)
