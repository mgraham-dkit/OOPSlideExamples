class MusicPlayer:
    # Define a static (shared) variable
    # Every copy of MusicPlayer (i.e. every object) will share a single count
    # This will be used to track the last generated ID value
    count = 0
    
    # Define the constructor and allow for an optional library list to be supplied
    def __init__(self, owner, library=[]):
        # Store the supplied owner information
        self.owner = owner
        # Increase the count of generated/created objects by 1
        MusicPlayer.count+=1
        # Set THIS INSTANCE'S id to be equal to the current number of objects that exist
        # When the first object is made, the count of objects goes to 1
        # and the first object's ID is then set to 1
        # When the second object is made, the count of objects goes to 2
        # and the second object's ID is then set to 2
        # However, the first object's ID stays at 1
        self.id = MusicPlayer.count
        # Store the supplied library information
        self.library = library
    
    # Define a function to display information about the current instance
    def display(self):
        # Include the static information - this will be the same no matter
        # which object you display
        # Access the static information using MusicPlayer.count (i.e.
        # the count belonging to the MusicPlayer class)
        # Access the instance information using self.id, self.owner and self.library
        # (i.e. the information belonging to the current instance of MusicPlayer)
        print(f"MusicPlayer[Count={MusicPlayer.count}, id={self.id}, owner={self.owner}, library={self.library}]")
        