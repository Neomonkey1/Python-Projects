
# This function receive user input
def getInfo():
    var1 = input('\nPlease provide the first numric value: ')
    var2 = input('\nPlease provide the second numric value: ')
    return var1,var2

# This function computes user input
def compute():
    #adding while loop with bool condition to keep program going till finished
    go = True
    while go:
        var1,var2 = getInfo()
        #added try to function 
        try:
            var3 = int(var1) + int(var2)            
            go = False
        #added except to catch an error the user might put in
        #added the ValueError to catch anything that isn't a numric value
        except ValueError as e:
            print('{}: \n\nYou did not provide a numric value.'.format(e))
        #added this except for unknown errors    
        except:
            print('\nOops, you provided invalid input, program will close now!')
    print('{} + {} = {}'.format(var1, var2, var3))



if __name__ == "__main__":

    compute()
