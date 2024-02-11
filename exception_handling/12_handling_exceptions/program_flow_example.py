try:
    num = int(input("Please enter a number: "))
    print(f"{num} squared is {num*num}")
except Exception as e:
    print(f"An Exception occurred: {type(e)}")
    print("You must enter a number.")

print("Thanks for using the squaring program")

