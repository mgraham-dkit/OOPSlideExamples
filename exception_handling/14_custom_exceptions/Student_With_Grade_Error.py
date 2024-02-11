from GradeError import GradeError


class Student:
    top_grade = None

    def __init__(self, id_num, name, year, grades=[]):
        self.id_num = id_num
        self.name = name

        if year < 0 or year > 4:
            raise ValueError("Inappropriate year value supplied - Maximum of 4 years possible")
        self.year = year

        student_max = ("None", -1)
        for grade in grades:
            if not isinstance(grade, tuple):
                # Instead of raising standard exceptions, we raise a custom exception specific to our own logic
                raise GradeError(f"Grades must be provided in as tuples. Grade provided as: {grade}")
            if len(grade) != 2:
                raise GradeError(f"Grades must be provided in format: (Module name, grade achieved). Grade provided as: {grade}")
            if not isinstance(grade[1], int) and not isinstance(grade[1], float):
                raise GradeError(f"Grade value must be provided as a number (int or float). Grade provided: {type(grade[1])}")
            if grade[1] < 0 or grade[1] > 100:
                raise GradeError(f"Grade cannot be less than 0 or over 100. Grade provided: {grade[1]}")

            if grade[1] > student_max[1]:
                student_max = grade

        self.grades = grades
        if Student.top_grade is None:
            Student.top_grade = student_max
        elif student_max[1] > Student.top_grade[1]:
            Student.top_grade = student_max

    def __repr__(self):
        return f"Student(id={self.id_num}, name={self.name}, year={self.year}, grades={self.grades}, top_grade={Student.top_grade})"