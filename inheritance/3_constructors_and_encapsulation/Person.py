# Define a class called Person (this should be in a file called Person.py)
class Person:
    # Declare that a Person contains three attributes
    # This gives every Person object 3 pieces of data to store
    fName = "Joe"
    lName = "Bloggs"
    age = 18
    
    # Define how a Person object can be created (a constructor)
    # This states that when a Person object is made, 3 values must be provided
    # We also have to supply self as the first parameter, so that python knows
    # WHICH Person to set the information for
    # The constructor's code should set up the new object in whatever way
    # you think is appropriate for the system - think of it as the set up stage
    def __init__(self, fName, lName, age):
        # Store the fName value provided by the calling code in the fName attribute (self.fName)
        self.fName = fName
        # Store the lName value provided by the calling code in the lName attribute (self.lName)
        self.lName = lName
        # Store the age value provided by the calling code in the age attribute (self.age)
        self.age = age
    
    # Define a display method to print out the information of the current person objcet
    # self is specified as a parameter so this method knows whose version of the attributes to use
    def display(self):
        print(f"First name: {self.fName}")
        print(f"Last name: {self.lName}")
        print(f"Age: {self.age}")