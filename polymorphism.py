

#Parent Class User
class User:
    name = "Teran"
    email = "Teran@gmail.com"
    password = "123abc"
#Creates a method function for user to input info
    def getLoginInfo(self):
        entry_name = input("enter your name: ")
        entry_email = input("enter your email: ")
        entry_password = input("enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The password or email is incorrect.")

#First Child Class Employee
class Employee(User):
    base_pay = 11.00
    department = "General"
    pin_number = "3980"


#This is the same method in the parent class "User".
#The difference is that, instead of using entry_password, we're using entry_pin.

    def getLoginInfo(self):
        entry_name = input("enter your name: ")
        entry_email = input("enter your email: ")
        entry_pin = input("enter your pin: ")
        if (entry_email == self.email and entry_pin == self.pin_number):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The pin or email is incorrect.")

#Second Child Class Customer
class Customer(User):
    member_status = "Platinum"
    rewards_memberID = "5454"
    password = "3999"

#This is the same method in the parent class "User".
#The difference is that, instead of using entry_email, we're using entry_rewards_memberID.

    def getLoginInfo(self):
            entry_name = input("enter your name: ")
            entry_rewards_memberID = input("enter your rewards member ID: ")
            entry_password = input("enter your password: ")
            if (entry_rewards_memberID == self.rewards_memberID and entry_password == self.password):
                print("Thanks for being a rewards member, {}!".format(entry_name))
            else:
                print("The password or Member ID is incorrect.")


member = Customer()
member.getLoginInfo()

manager = Employee()
manager.getLoginInfo()

