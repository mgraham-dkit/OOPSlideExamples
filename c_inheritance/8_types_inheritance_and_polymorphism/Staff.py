class Staff:
    def __init__(self, fName, lName, dept):
        self.fName = fName
        self.lName = lName
        self.dept = dept

    def generate_email(self):
        dept = self.dept.replace(" ", "_")
        return f"{self.fName[0].lower()}{self.lName.lower()}.{dept.lower()}@workdomain.com"


    def display(self):
        print(f"Staff[fName={self.fName}, lName={self.lName}, dept={self.dept}]")