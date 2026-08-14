class Comp:
    Emp_count = 0

    def __init__(self, name, salary, bouns):
        self.name = name
        self.salary = salary
        self.bouns = bouns

        Comp.Emp_count += 1

    def Cal_bouns(self):
        self.total_sal = self.salary + self.bouns

    def display(self):
        print(
            f"Name: {self.name}, "
            f"Bonus: {self.bouns}, "
            f"Total Salary: {self.total_sal}, "
            f"Employee Count: {Comp.Emp_count}"
        )


C = Comp("Aarav", 25000, 1250)
C.Cal_bouns()
C.display()

C1 = Comp("Aakash", 25000, 1250)
C1.Cal_bouns()
C1.display()

C2 = Comp("manish", 25000, 1250)
C2.Cal_bouns()
C2.display()