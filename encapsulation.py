# Encapsulation is emplemented by using private and protected attributes and functions
# this makes it harder for functions and properties to be modified


# creating a class with a protected variable that is prefixed with a single underscore
# it acts as a warning to other developers not to use it outside of the class
class Protected:
    def __init__(self):
        self._protectedVar = 5

obj = Protected() # obj is used to modify the value
obj._protectedVar = 50
print(obj._protectedVar) #prints the new value

# Private variables are denoted with a double underscore prefix
class Protected:
    def __init__(self):
        self.__privateVar = 10

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar = private

# obj gets the data of the private variable 
obj = Protected()
obj.getPrivate()    # returns the origanal value set 
obj.setPrivate(25)  # obj also sets a new value to privateVar
obj.getPrivate()    # returns the new value 
