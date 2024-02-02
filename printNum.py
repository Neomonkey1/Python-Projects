
import ourModule
import datetime
import random

# This part uses ourModule
if __name__ == '__main__':
  results = ourModule.getNumbers(5,9)
  print(results)
# This uses the datetime module
A = datetime.datetime.now()
print(A)
# This uses the random module
print(random.randrange(1,100))
