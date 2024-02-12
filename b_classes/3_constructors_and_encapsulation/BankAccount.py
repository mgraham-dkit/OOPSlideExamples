# Define a class called BankAccount (this should be in a file called BankAccount.py)
class BankAccount:
    # Specify that it includes two public attributes
    # Each contains a default value
    fName = "Joe"
    lName = "Bloggs"
    # Specify that it includes a single private attribute with a default value of 0
    # By starting its name with __, we are locking direct access to the variable
    # to only this class
    __balance = 0
    
    # Create a constructor that requires two parameters, with a third optional parameter
    # Where only two values are provided, the value for __balance defaults to 0
    # Where three values are provided, the value supplied in the __balance
    # position is used for __balance
    def __init__(self, fName, lName, __balance=0):
        # Store the supplied value for fName in the fName attribute
        self.fName = fName
        # Store the supplied value for lName in the lName attribute
        self.lName = lName
        # Store the supplied (or default) value for __balance in the __balance attribute
        self.__balance = __balance
    
    # Define a display method to print out the information of the current bank account
    # self is specified as a parameter so this method knows whose version of the attributes to use
    def display(self):
        print(f"BankAccount[first name: {self.fName}, last name: {self.lName}, balance: {self.__balance}]")
        
    # Getter method to retrieve the current value of __balance
    # This is needed because __balance is a private variable,
    # i.e. only this class can access it directly (using self.__balance)
    def get_balance(self):
        return self.__balance
    
    # Setter method to change the value of the __balance attribute
    # This is needed because __balance is a private variable
    def set_balance(self, new_bal):
        # If the new balance value is below 0, do not change the __balance value
        if new_bal > 0:
            self.__balance = new_bal
        else:
            print("No overdraft enabled")
            
            