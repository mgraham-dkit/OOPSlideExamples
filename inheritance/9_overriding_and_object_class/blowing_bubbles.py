# Import Circle and Sphere classes
from Circle import Circle
from Sphere import Sphere
# Import random module
import random

# Create a function to display a list of circles/spheres using their display method
def display_list(data):
    for elem in data:
        elem.display()


# Create a list of colours which we can select from at random
colours=["red", "blue", "green", "yellow", "orange", "indigo", "violet"]
# Create a blank list to store the randomly created circles
circles = []

# Take in how many objects to randomly create
quantity = int(input("Please enter the number of circles to be made: "))
# Loop to create the specified number
for i in range(quantity):
    # Take in core information:
    # randomly generate a radius
    radius = random.randint(0, 20)
    # Select a colour from the list at random
    colour = random.choice(colours)

    # Generate a random number between 1 and 2 - this is the equivalent of a coin flip
    # and we can use it to decide whether to make a circle or sphere
    type = random.randint(1, 2)
    # Build the appropriate type
    if type == 1:
        shape = Circle(radius, colour)
    else:
        shape = Sphere(radius, colour)

    # Add the new shape to the list
    circles.append(shape)

# Print all shapes from the list
display_list(circles)