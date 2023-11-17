from Staff import Staff
from FullTimeStaff import FullTimeStaff
from PartTimeStaff import PartTimeStaff


employee = Staff("Michelle", "Graham", "Computing and Maths")
print(employee.generate_email())
employee.display()

full_timer = FullTimeStaff("Ghosty", "McBooson", "ICAM", 54000, ["office hire expenses", "Wellness support", "Pension matching"])
full_timer.display()

part_timer = PartTimeStaff("Mireya", "Alemida", "Humanities", 89, 9.35)
part_timer.display()

# Detecting the type of instances
staff = [employee, full_timer, "Fake staff member, not a staff object", part_timer]
for person in staff:
    # When checking, go from most specific to most general (i.e. check subclass types before superclass types)
    if isinstance(person, FullTimeStaff):
        print(f"{person.fName} is a full-time staff member")
        print(f"Their salary is: {person.salary}")
    elif isinstance(person, PartTimeStaff):
        print(f"{person.fName} is a part-time staff member.")
        print(f"Their wage was: {person.calc_wage()}")
    elif isinstance(person, Staff):
        print(f"{person.fName} is a staff member")
    else:
        print(f"\"{person}\" is not a Staff instance")