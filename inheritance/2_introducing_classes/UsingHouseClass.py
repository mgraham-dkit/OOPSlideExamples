# Import the class called House from the module/file called House(.py)
from House import House


# Create an instance of the House class (i.e. create a House)
my_home = House()
# Change the number of rooms in this house to be 20
my_home.num_rooms = 20
# Display the my_home object's num_rooms information
print(f"My house now has", my_home.num_rooms, "rooms\n")

# Call the display() method on my_home
# It will run the display() method belonging to the my_home object
# and use its data in the method code
# Even though the method has a parameter in its signature (line 13 of House.py)
# we do not write it in here. It is supplied by python behind the scenes.
my_home.display()
# Call the cost_to_paint() method belonging to my_home and display the result
print("The cost to paint this house is:",my_home.cost_to_paint(28))
