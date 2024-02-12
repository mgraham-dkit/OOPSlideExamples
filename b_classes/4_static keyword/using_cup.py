# Import the class
from Cup import Cup


# Create a Cup instance and give it custom values
my_mug = Cup("I heart Programming!", "Blue")
# Print out its information
my_mug.display()
# Change the dimensions of all mugs
my_mug.change_dimensions(10, 10)
# Print out its information
my_mug.display()

# Display the volume for all mugs
print(f"My mug's volume is: {Cup.calc_volume()}")