myDictionary = {'index1': 1, 'index2': 2, 'index3': 355}
print(myDictionary)
print(myDictionary['index2'])

dic_users = {'em_1234': {'fname': 'Bob', 'lname': 'Smith', 'phone': '132-456-7890'},
             'em_1235': {'fname': 'Mary', 'lname': 'Jones', 'phone': '132-364-5764'} }
print(dic_users['em_1235'])
print(dic_users['em_1235']['phone'])
print('User: {} {}\nPhone: {}'.format(dic_users['em_1235']['fname'],dic_users['em_1235']['lname'],dic_users['em_1235']['phone']))
# making a dictionary 
dic_car = {'brand': 'chevy', 'model': 'trax', 'year': 2021}
print(dic_car)
# using the get() method
A = dic_car.get('model')
print(A)
#changing the value of year
dic_car['year']=2022
print(dic_car)
#adding a item to the dictionary
dic_car['color']= 'white'
print(dic_car)
#making a nested dictionary
myFamily = {
    'child1' : {
        'name': 'Luke',
        'year': 2012
        },
    'child2' : {
        'name': 'Elijah',
        'year': 2023
        }
    }
print (myFamily)
#using the fromkeys() method
B = ('num1', 'num2', 'num3')
C = 0
num_dict = dict.fromkeys(B, C)
print(num_dict)
