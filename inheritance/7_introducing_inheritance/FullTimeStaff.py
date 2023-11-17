from Staff import Staff


class FullTimeStaff(Staff):
    def __init__(self, fName, lName, dept, salary, benefits=["Health insurance"]):
        super().__init__(fName, lName, dept)
        self.salary = salary
        self.benefits = benefits

    def add_benefit(self, new_benefit):
        if new_benefit not in self.benefits:
            self.benefits.append(new_benefit)
            return True
        return False

    def display(self):
        super().display()
        print(f"FullTimeStaff[salary={self.salary}, benefits={self.benefits}, email={self.generate_email()}]")