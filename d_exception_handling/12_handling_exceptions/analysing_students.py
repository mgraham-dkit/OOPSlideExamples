filename = "students.txt1"
read = False
while not read:
    grades = []
    try:
        with open(filename) as file_handle:
            for line in file_handle:
                components = line.strip().split("%%")
                try:
                    grades.append(int(components[1]))
                except ValueError as e:
                    print("Oh no, a value error occurred! Details:", e.args)
                    print("Skipping over record:", line.strip())
                except IndexError as e:
                    print("Insufficient components included in line. Details:", e.args)
                    print("Skipping over record:", line.strip())
        read = True
    except FileNotFoundError as e:
        print("uh oh! An exception of type:", e.__class__.__name__)
        filename = input("Please enter a VALID filename: ")


print("File was read in successfully!")
print(f"Grades for this classgroup: {grades}")