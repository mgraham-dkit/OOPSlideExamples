# Import the math module so we can get access to math.pi (needed in volume calculation)
import math


class Cup:
    # Define two static (shared) variables
    # Every copy of Cup (i.e. every object) will share a single height
    # and a single width
    height = 4
    width = 3
    
    def __init__(self, slogan="Insert Your Text", colour="white"):
        # No need to set the height and width in here,
        # they're already given default values
        
        # You don't tend to set static values based on parameter values in
        # a constructor, because constructors are about building a specific instance
        # while static variables are about ALL instances at once
        self.slogan = slogan
        self.colour = colour
        
    def display(self):
        # To access the static variables, we shouldn't use self.
        # (we can, but we shouldn't!)
        # Instead, because the variables belong to the class, we access them
        # with the class name (Cup.height and Cup.width)
        print(f"height={Cup.height}, width={Cup.width}, slogan={self.slogan}, colour={self.colour}")
    
    # Specify that the following method belongs to the class as a whole
    # using a decorator (@classmethod)
    # By specifying it's a class method and not just a static method, it
    # allows us to take in cls as the first parameter (just like self would be)
    @classmethod
    def change_dimensions(cls, new_height, new_width):
        # Set the height and width to the supplied values
        # this will change the data in these variables for every instance of this class
        # Remember, we need to refer to the variables either as Cup. or cls.
        # cls is better as we get the full picture about the entity
        cls.height = new_height
        cls.width = new_width
    
    # Specify that the following method belongs to the class as a whole
    # using a decorator (@staticmethod)
    # By specifying it's a static method, not a complete class method,
    # we limit the access the method will have - it does not get cls as a parameter
    @staticmethod
    def calc_volume():
        # Calculate the volume for any mug
        # As this method is a staticmethod, it does not have cls as a parameter,
        # so we have to access the variables using the classname
        # (Cup.height and Cup.width)
        volume = Cup.height*(math.pi*(Cup.width/2))
        return volume
        