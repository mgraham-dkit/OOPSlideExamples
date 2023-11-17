# Function to display dictionary content in a formatted manner
def print_dict(my_dict):
    # Print a line of -s to clearly define the start and end of the dictionary content
    print("-"*20)
    '''
        Retrieve all items (key-value pairs) from the dictionary,
        storing the key in k and the value in v 
        
        items() returns a tuple, so we need to specify that we're extracting from a tuple  
        in our argument unpacking, i.e. (k, v)
    '''
    for i, (k, v) in enumerate(my_dict.items()):
        # Print out the key and value from the current item
        print(f"{i}) Key: {k} -> Value: {v}")
    print("-" * 20)


# Create a dictionary containing 4 items (key-value pairs) matching a hostname to an IP address
dns = {
    "localhost" : "127.0.0.1",
    "google.com" : "196.23.12.8",
    "moodle.dkit.ie" : "234.122.35.1",
    "dkit.ie" : "234.122.44.12"
}
print_dict(dns)
# Wipe entry for moodle - set the IP address value to None
dns["moodle.dkit.ie"] = None

# Find all routes to dkit
# in this example a route to DkIT is indicated by the IP starting with 234.122
# Create a blank dictionary
dkit_routes = {}
# Loop through the entries in our dns dictionary
for k, v in dns.items():
    # Check that the current item has an IP address associated (i.e. not None)
    # AND that that IP address starts with the required values
    if v is not None and v[0:7] == "234.122":
        # If the current item is for a dkit route, add it to the dkit_routes dictionary
        dkit_routes[k] = v

# Display the routes dictionary
print_dict(dkit_routes)