# Import the Person class from the Person.py module file
from Person import Person


# Create a Person instance called p1 using its parameterised constructor.
# This will create a Person object in memory with a fName of "Ariel",
# an lName of "the Mermaid" and an age of 16
p1 = Person("Ariel", "the Mermaid", 16)
# Print out p1's data
p1.display()