from abc import ABC, abstractmethod

# making parent class Payment with (Abstract Base Class) 
class Payment(ABC):
    def payAmount(self, amount):
        print("The amount you owe is $",amount)
# using the @abstractmethod we can pass in an argument from another source without knowing what data it will be.
    @abstractmethod
    def payment(self, amount):
        pass

# making child class CreditCard 
class CreditCard(Payment):
# Define how to implement the payment function from parent class
    def payment(self, amount):
        print("The amount of ${} will be charged to your Credit Card.".format(amount))

# making child class GiftCard
class GiftCard(Payment):
# Define how to implement the payment function from parent class
    def payment(self, amount):
        print("${} will be used from your Gift Card.".format(amount))

#Making child class CreditCard a var to use payAmount and payment functions
obj1 = CreditCard()
#adding amount data here
obj1.payAmount(250)
obj1.payment(250)

#Making child class GiftCard a var to use payAmount and payment functions
obj2 = GiftCard()
#adding amount data here
obj2.payAmount(150)
obj2.payment(150)
