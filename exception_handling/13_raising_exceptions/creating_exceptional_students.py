from Student import Student


valid_file = False
while not valid_file:
    try:
        filename = input("Please enter the filename for student data (including relative path): ")
        students = []
        with open(filename) as file:
            valid_file = True
            for line in file:
                line = line.strip()
                student_data = line.split("%%")
                if len(student_data) == 4:
                    id = student_data[0]
                    name = student_data[1]
                    try:
                        year = int(student_data[2])
                        grade_data = student_data[3].split("~~")
                        grades = []
                        for grade in grade_data:
                            module, score = grade.split("__")
                            grades.append((module, float(score)))

                        student = Student(id, name, year, grades)
                        students.append(student)
                        print(f"Student {student} added to the list")
                    except ValueError as e:
                        print(f"Numeric type issue with student record: {line}")
                        print(e)
                else:
                    print(f"Inappropriate amount of data supplied for student: {line}")

    except FileNotFoundError as e:
        print("No such file was found. Please try again.")