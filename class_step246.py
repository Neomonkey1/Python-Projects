


#Creating parent class Vehicle
class Vehicle:    
    style = 'car'
    doors = 4
    vin_num = 'vn1234'
    
    #method to identify
    def identify(self):
        entry_style = input('Enter style of vehicle: ')
        entry_vin_num = input('Enter vin number: ')
        if (entry_style == self.style and entry_vin_num == self.vin_num):
            print("That vin number matches your {} .".format(self.style))
        else:
            print("No vehicle matches that vin number.")

#Creating child class Ford
class Ford(Vehicle):
    color = 'blue'
    model = 'fusion'
    lease_num = 'lc777'

    #method to identify
    #using lease_num instead of vin_num to identify
    def identify(self):
        entry_model = input('Enter model of vehicle: ')
        entry_lease_num = input('Enter your lease number: ')
        if (entry_model == self.model and entry_lease_num == self.lease_num):
            print("Confirm, your lease for the {} is good.".format(self.model))
        else:
            print("Incorrect, please check model and lease number.")

#Creating child class Toyota 
class Toyota(Vehicle):
    color = 'White'
    model = 'camry'
    lease_num = 'lc666'

    #method to identify using lease_num instead of vin_num to identify
    def identify(self):
        entry_model = input('Enter model of vehicle: ')
        entry_lease_num = input('Enter your lease number: ')
        if (entry_model == self.model and entry_lease_num == self.lease_num):
            print("Confirm, your lease for the {} is good.".format(self.model))
        else:
            print("Incorrect, please check model and lease number.")






if __name__ == '__main__':
    X = Vehicle()
    X.identify()

    Y= Ford()
    Y.identify()

    Z = Toyota()
    Z.identify()
