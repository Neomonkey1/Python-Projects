myDictionary = {'index1': 1, 'index2': 2, 'index3': 355}
print(myDictionary)
print(myDictionary['index2'])

dic_users = {'em_1234': {'fname': 'Bob', 'lname': 'Smith', 'phone': '132-456-7890'},
             'em_1235': {'fname': 'Mary', 'lname': 'Jones', 'phone': '132-364-5764'} }
print(dic_users['em_1235'])
print(dic_users['em_1235']['phone'])
print('User: {} {}\nPhone: {}'.format(dic_users['em_1235']['fname'],dic_users['em_1235']['lname'],dic_users['em_1235']['phone']))
