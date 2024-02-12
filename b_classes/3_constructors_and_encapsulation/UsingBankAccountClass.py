# Import the BankAccount class from the BankAccount.py module file
from BankAccount import BankAccount


# Create a BankAccount instance called my_acc using its parameterised constructor.
# This will create a BankAccount object in memory with a fName of "Michelle" and 
# an lName of "Graham". As I haven't supplied the optional balance value,
# the object's balance will be set to 0
my_acc = BankAccount("Michelle", "Graham")
# As the balance variable is private (because its name starts with __), we can't
# use my_acc.__balance. Therefore we have to use a method to get that value
# To see the impact of the private setting, try replacing .get_balance()
# with .__balance in the line below
print("Michelle's current balance is €", my_acc.get_balance())
print(isinstance(my_acc, BankAccount))
