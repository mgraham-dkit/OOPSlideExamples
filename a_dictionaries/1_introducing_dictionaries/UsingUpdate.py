def print_dict(my_dict):
    # Print a line of -s to clearly define the start and end of the dictionary content
    print("-" * 20)
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


phone_book = {
    "Helen": "+353 87 669 1203", 
    "Alan": "+353 88 291 3048", 
    "Fiona": "+353 86 214 5734"
}
supplemental = {
    "Helen": "DIFFERENT", 
    "Alanna": "+353 88 291 2348", 
    "Fiona (Alt)": "+353 85 299 5734"
}
phone_book.update(supplemental)
print_dict(phone_book)
