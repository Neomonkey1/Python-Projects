

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
