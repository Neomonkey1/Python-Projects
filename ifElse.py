num1 = 12
key = False
# using different if else and elif statements 

if num1 == 12:
    if key:
        print('num1 is equal to twelve and they have the key')
    else:
        print('num1 is equal to twelve and they do NOT have the key')
elif num1 < 12:
    print('num1 is less than twelve')
else:
    print('num1 is not equal to twelve')

# more if else and elif statements

A = 200
B = 20
C = 100

if B > A:
    print('B is greater than A')
elif A == B:
    print('A and B are equal')
else:
    print('A is greater than B')
# short hand if statement

if C > B: print('C is greater than B')

# nested if

if B > 10:
    print('Above ten, ')
    if B > 30:
        print('and also above 30!')
    else:
        print('but not above 30.')

# Boolean values. Boolean values are True or False
print(bool('Hello'))
print(bool(20))
D = 'Hey'
print(bool(A))
print(bool(D))
if C > B: print('C is greater than B')
bool(False)
bool(None)
bool(0)
bool('')
bool(())
# boolean isinstance()
print(isinstance(A, int))

