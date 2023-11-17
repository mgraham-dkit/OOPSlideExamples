# Create a contact dictionary
phone_book = {
    "Helen": "+353 87 669 1203",
    "Alan": "+353 88 291 3048",
    "Fiona": "+353 86 214 5734"
}
name = "Helen"
# Check if a specific key appears in the phone_book (in will check the keys, not values)
if name in phone_book:
    # Key was found in the phone book, so we display the corresponding value
    print(f"{name} was found in the phone book. Its value is:", phone_book[name])
else:
    # Key was not found in the phone book
    # We should always inform the user in both situations (success and failure!)
    print(f"{name} was not found in the phone book.")

new_name = input("Please enter the new contact's name:\n")
# If the contact name is not already a key in the phone book (not in), we can add the new contact info
if new_name not in phone_book:
    # If the contact name is not already there, we can now take in the corresponding phone number
    new_num = input(f"Please enter {new_name}'s phone number:\n")
    # Add the new contact's information to the phone book
    phone_book[new_name] = new_num
else:
    print(f"Sorry, the name \"{new_name}\" is not available.")
