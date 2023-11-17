# Create a dictionary to hold contact information
# The key is the contact's name
# The value is the contact's (formatted) phone number
phone_book = {
    "Helen": "+353 87 669 1203",
    "Alan": "+353 88 291 3048",
    "Fiona": "+353 86 214 5734"
}
# Add a new item (key-value pair) to the dictionary
phone_book["New Friend"] = "+353 85 9739 221"
# Update an existing item (if there is nothing with the key "Fiona", this will crash
phone_book["Fiona"] = "Changed!"
print(phone_book)

# Print a line of -s to clearly define the start of the key information
print("-" * 20)
print("Keys:")
# Get all keys stored in the phone book (this will NOT get any corresponding values)
keys = phone_book.keys()
# Loop through the keys and display them in a formatted manner
for i, k in enumerate(keys):
    print(f"{i+1}) {k}")

print("-" * 20)
print("Values:")
# Get all values stored in the phone book (this will NOT get any corresponding keys)
values = phone_book.values()
# Loop through the values and display them in a formatted manner
for i, v in enumerate(values):
    print(f"{i+1}) {v}")

print("-" * 20)
print("Items:")
# Get all elements in a dictionary
items = phone_book.items()
# Loop through the items and display them in a formatted manner
# As an item contains a key and a value, this will display both parts for each one
for i, item in enumerate(items):
    print(f"{i+1}) {item}")