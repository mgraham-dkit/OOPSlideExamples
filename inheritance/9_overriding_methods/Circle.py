# Import the math module for pi constant
import math

# Define a Circle class
class Circle:
    # Constructor defining attributes / instance variables for each Circle
    # Colour is an optional parameter, if it's not supplied then the default value ("Blue") is used
    def __init__(self, radius, colour="Blue"):
        # Store radius and colour information
        self.radius = radius
        self.colour = colour

    # Create a function to calculate the area of the circle
    def calc_area(self):
        # Formula for area of a circle: pi * r^2
        # Return calculation of area using math.pi as value for pi
        return math.pi*(radius*radius)

    # Create a function to display the circle's data
    def display(self):
        # Print out the pieces of the circle
        print(f"Circle[radius={self.radius}, colour={self.colour}]")