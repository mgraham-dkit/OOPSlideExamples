# Define a class called House (This should be in a file called House.py)
class House:
    # Define the attributes of a House
    # This specifies what information will be stored about every House created
    # Each attribute gets default values
    window_type = "Bay"
    num_rooms = 10
    colour = "Beige"

    # Define a method called display that prints out the current House's info
    # We must take self as a parameter so the method knows
    # which object is being worked with
    # We have to refer to the attributes as self.name so python knows we want to
    # use this object's version of them
    def display(self):
        print(f"Window type = {self.window_type}")
        print(f"Number of rooms = {self.num_rooms}")
        print(f"Colour = {self.colour}")
        
    # Define a method called cost_to_paint that takes in the cost of paint and
    # calculates how much it will cost to paint all of the rooms if every room
    # needs 5l of paint to complete it
    # We have to refer to the attributes as self.name so python knows we want to
    # use this object's version of them (note how we don't do it on paint_price)
    def cost_to_paint(self, paint_price):
        return self.num_rooms * (paint_price * 5)
    