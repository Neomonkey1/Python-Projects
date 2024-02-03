# functions will use local variables
# if no local variables functions will use globe variables
#globe variable
name = 'Python'

# function using globe variable
def getName():
    print('I am coding with {}'.format(name))

getName()

# function using local variable
def getName2():
    # local variable
    name = 'C#'
    print('I am coding with {}'.format(name))

getName2()
