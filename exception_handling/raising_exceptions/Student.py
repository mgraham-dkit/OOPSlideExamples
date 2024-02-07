class Student:
    top_grade = None

    def __init__(self, id, name, year, grades=[]):
        self.id = id
        self.name = name

        if year < 0 or year > 4:
            raise ValueError("Inappropriate year value supplied - Maximum of 4 years possible")
        self.year = year

        student_max = ("None", -1)
        for grade in grades:
            if not isinstance(grade, tuple):
                raise TypeError(f"Grades must be provided in as tuples. Grade provided as: {grade}")
            if len(grade) != 2:
                raise ValueError(f"Grades must be provided in format: (Module name, grade achieved). Grade provided as: {grade}")
            if not isinstance(grade[1], int) and not isinstance(grade[1], float):
                raise TypeError(f"Grade value must be provided as a number (int or float). Grade provided: {type(grade[1])}")
            if grade[1] < 0 or grade[1] > 100:
                raise ValueError(f"Grade cannot be less than 0 or over 100. Grade provided: {grade[1]}")

            if grade[1] > student_max[1]:
                student_max = grade

        self.grades = grades
        if Student.top_grade is None:
            Student.top_grade = student_max
        elif student_max[1] > Student.top_grade[1]:
            Student.top_grade = student_max


    def __repr__(self):
        return f"Student(id={self.id}, name={self.name}, year={self.year}, grades={self.grades}, top_grade={Student.top_grade})"