# Import the logging module
import logging


class Student:
    """
        Class to model a Student. Student grades are held in a list.
        Each grade is held as a tuple structured as: (module_name (str), grade (a float))
        The highest grade across all created Student objects is stored in a static variable
        called top_grade.
    """
    # Static (shared) variable because it's created outside methods and doesn't include a reference to self.
    top_grade = None

    # Static logger variable to log all issues to do with Students
    logger = logging.getLogger(__name__)

    # Create a constructor to build a Student
    def __init__(self, id_num, name, year, grades=[]):
        """
            Create an instance of Student. If the new Student has a grade higher than the current top_grade
                for all Students, the top_grade is updated.

            :param str id_num: The id number of the student
            :param str name: The name of the student
            :param int year: The current college year of the student (Year must be between 1 and 4)
            :param list[(str, float)] grades: A list of the student's grades.
                (Duplicate module names are permitted. Grade values must be between 1 and 100).
            :raises ValueError: Where the year, the length of a grade tuple or a grade value supplied are inappropriate.
            :raises TypeError: Where grades are not provided as tuples or grade values are not provided as numbers
                (either float OR int)
        """

        # Store supplied id and name information
        self.id_num = id_num
        self.name = name

        # Check if the year is valid
        if year <= 0 or year > 4:
            # Log the issue with the year using the logger
            # As this cannot be recovered without intervention from the user
            # We use the error level
            Student.logger.error(f"Year {year} not an appropriate value.")
            raise ValueError("Inappropriate year value supplied - Maximum of 4 years possible")
        # If the year provided is allowable, save it
        self.year = year

        # Create a variable to track the highest grade for THIS student
        student_max = ("None", -1)
        # Loop through all the supplied grade tuples
        for grade in grades:
            # Check if the current grade is not a tuple
            if not isinstance(grade, tuple):
                # Log the issue with the grade using the logger
                # As this cannot be recovered without intervention from the user, we use the error level
                Student.logger.error(f"Grade {grade} not in tuple format")
                raise TypeError(f"Grades must be provided as tuples. Grade provided as: {grade}")
            # If there are not enough pieces in the grade to be valid (need 2 - a module name and a grade value)
            if len(grade) != 2:
                # Log the issue with the grade using the logger
                # As this cannot be recovered without intervention from the user, we use the error level
                Student.logger.error(f"Grade {grade} does not contain the right number of components")
                raise ValueError(f"Grades must be provided in format: (Module name, grade achieved). Grade provided as: {grade}")
            # If the grade value is not a number (either int OR float)
            if not isinstance(grade[1], int) and not isinstance(grade[1], float):
                # Log the issue with the grade using the logger
                # As this cannot be recovered without intervention from the user, we use the error level
                Student.logger.error(f"Grade value in {grade} not in numeric form")
                raise TypeError(f"Grade value must be provided as a number (int or float). Grade provided: {type(grade[1])}")
            # If the grade value provided is too big or too small
            if grade[1] < 0 or grade[1] > 100:
                # Log the issue with the grade using the logger
                # As this cannot be recovered without intervention from the user, we use the error level
                Student.logger.error(f"Grade value in {grade} not within legal range for a grade")
                raise ValueError(f"Grade cannot be less than 0 or over 100. Grade provided: {grade[1]}")

            # If all the validation checks pass for this grade,
            # check if it's higher than the current max for this student
            # If it is, then update the current max
            if grade[1] > student_max[1]:
                student_max = grade

        # If all validation checks pass for EVERY grade, then save the list of grades as the student's grades
        # (Remember, the only way we could get to here is if we haven't raised any exceptions,
        # so the validation checks must all have passed)
        self.grades = grades
        # If this is the first Student created, the top_grade hasn't been changed from the default yet
        # (and is still None)
        if Student.top_grade is None:
            # As the highest grade is being changed for all Students, we can log an info message
            Student.logger.info(f"Max grade changed. Was {Student.top_grade}, is now {student_max}")
            # Set this student's highest grade to be the highest grade for all students
            Student.top_grade = student_max
        # If this student's grade is higher than the current top grade
        elif student_max[1] > Student.top_grade[1]:
            # As the highest grade is being changed for all Students, we can log an info message
            Student.logger.info(f"Max grade changed. Was {Student.top_grade}, is now {student_max}")
            # Set this student's highest grade to be the highest grade for all students
            Student.top_grade = student_max

    def __repr__(self):
        """Returns a string representation of all data in the Student class (includes variable names)"""
        return f"Student(id={self.id_num}, name={self.name}, year={self.year}, grades={self.grades}, top_grade={Student.top_grade})"