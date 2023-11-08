from Staff import Staff


class PartTimeStaff(Staff):
    def __init__(self, fName, lName, dept, hours_worked, hourly_rate = 10.50):
        super().__init__(fName, lName, dept)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calc_wage(self):
        if self.hours_worked < 10:
            gross_pay = 10 * self.hourly_rate
        else:
            gross_pay = self.hours_worked * self.hourly_rate

        return gross_pay

    def display(self):
        print(f"PartTimeStaff[fName={self.fName}, lName={self.lName}, dept={self.dept}, "
              f"hours_worked={self.hours_worked}, hourly_rate={self.hourly_rate}]")