class Teacher:
    def teaching(self):
        print("Teacher is teaching")


class Student:
    def studying(self):
        print("Student is studying")


class Person(Teacher, Student):
    def details(self):
        print("Person can teach and study")


p = Person()

p.teaching()
p.studying()
p.details()