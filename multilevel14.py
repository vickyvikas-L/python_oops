class Person:
    def details(self):
        print("Name: Vikas")
        print("Age: 21")


class Student(Person):
    def marks(self):
        print("Python: 85")
        print("SQL: 90")


class Result(Student):
    def display(self):
        print("Result: Pass")


r = Result()

r.details()
r.marks()
r.display()