# Import the class
from MusicPlayer import MusicPlayer


# Create a MusicPlayer with a default library
my_zune = MusicPlayer("Michelle Graham")
# Display its information - it will have id == 1 because only one has been made
my_zune.display()
# Create a second music player and supply a library as well as owner info
backup_zune = MusicPlayer("Also Michelle Graham", ["Wildest Dreams", "Style"])
# Display its information - it will have id==2 because two have been made
backup_zune.display()
# The original music player will still have id == 1 as nothing has changed it
# The static variable has been changed, not this instance's variable
my_zune.display()