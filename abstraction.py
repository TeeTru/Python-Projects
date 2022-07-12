
# we are importing the "abstractmethod" from the abc(abstract base class) module
from abc import ABC, abstractmethod
class car(ABC):
    def paySlip(self, amount):
        print("Your purchase amount: ",amount)
# this function is telling us to pass in an argument, but we won't tell you how or what kind
# of data it will be.
    @abstractmethod
    def payment(self, amount):
        pass

# we created the child class 
class DebitCardPayment(car):
# here we've defined how to implement the payment function from its parent paySlip class.
    def payment(self, amount):
        print('Your purchase amount of {} exceeded your $100 limit '.format(amount))

obj = DebitCardPayment()
obj.paySlip("$500")
obj.payment("$500")


