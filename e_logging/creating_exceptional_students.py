import logging
from Student import Student


# Configure the logging settings for the application
student_fileHandler = logging.FileHandler(filename="student_log.txt", mode="a")
student_fileHandler.setLevel(logging.WARNING)
logging.basicConfig(format='%(asctime)s %(name)s.%(funcName)s +%(lineno)s: %(levelname)-8s [%(message)s]',
                    level=logging.INFO, handlers=[student_fileHandler])
# logging.basicConfig(filename="student_log.txt")

logger = logging.getLogger(__name__)
# Add an extra handler to the configuration to send debug messages to the console
# Note: This will ONLY kick in when the overall logging level is set to debug, otherwise they'll be ignored
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
logger.addHandler(console_handler)

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
                    id_num = student_data[0]
                    name = student_data[1]
                    try:
                        year = int(student_data[2])
                        grade_data = student_data[3].split("~~")
                        grades = []
                        for grade in grade_data:
                            module, score = grade.split("__")
                            grades.append((module, float(score)))

                        student = Student(id_num, name, year, grades)
                        students.append(student)
                        print(f"Student {student} added to the list")
                    except ValueError as e:
                        print(f"Numeric type issue with student record: {line}")
                        print(e)
                        logger.exception("Bad data provided")
                else:
                    print(f"Inappropriate amount of data supplied for student: {line}")

    except FileNotFoundError as e:
        print("No such file was found. Please try again.")
        logger.warning(f"Invalid filename provided: {filename}")