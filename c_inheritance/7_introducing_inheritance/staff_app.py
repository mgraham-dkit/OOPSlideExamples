import random as rand
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

employees = [employee, full_timer, part_timer]
# Shuffle the content of the list
rand.shuffle(employees)
print("*" * 20)
for i in range(len(employees)):
    print("-" * 10)
    print(f"{(i+1)}:")
    employees[i].display()
print("*" * 20)