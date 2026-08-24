class Student:
    def student_details(self):
        print("Name: Vikas")
        print("Roll No: 101")


class Marks:
    def marks_details(self):
        print("Python: 85")
        print("SQL: 80")


class Result(Student, Marks):
    def result(self):
        print("Result: PASS")


r = Result()

r.student_details()
r.marks_details()
r.result()