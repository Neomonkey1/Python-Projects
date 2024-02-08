

# Creating parent class

class Computer:
    #creating a dunder method to attach the arguments for creating the class object
    def __init__(self, brand, cpu, os, disk_space, ram):
        self.brand = brand
        self.cpu = cpu
        self.os = os
        self.disk_space = disk_space
        self.ram = ram

#creating child class
class Laptop(Computer):
    def __init__(self, brand, cpu, os, disk_space, ram, screen_size,battary_life):
        self.brand = brand
        self.cpu = cpu
        self.os = os
        self.disk_space = disk_space
        self.ram = ram
        self.screen_size = screen_size
        self.battary_life = battary_life


#adding arguments to make parent object
comp = Computer('Dell', 'Intel Core i7', 'Windows 11', '1 TB', '16 GB')

#adding arguments to make child class object
lapComp = Laptop('HP', 'Intel Corei7', 'Windows 11', '500 GB', '8 GB', '15 inch', '4 hours')


#adding a method
def myFunc(self):
    print('This Computer is a {} with an {} inside using {} with a {} hard drive and {} RAM'.format(self.brand,self.cpu,self.os,self.disk_space,self.ram))




if __name__ == '__main__':
    myFunc(comp)
    
    myFunc(lapComp)
    
    print(lapComp.battary_life,lapComp.screen_size)
    
