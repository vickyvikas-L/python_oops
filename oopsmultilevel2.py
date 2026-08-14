class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    student_count = 0

    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course
        Student.student_count += 1
    @classmethod
    def count_students(cls):
        print("Total students:", cls.student_count)

class PhDCandidate(Student):
    def __init__(self, name, age, course, thesis_title):
        super().__init__(name, age, course)
        self.thesis_title = thesis_title

    @staticmethod
    def validate_thesis(title):
        return len(title) > 20

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)
        print("Thesis:", self.thesis_title)

s1 = Student("Manish", 22, "BE")
s2 = Student("Druva", 21, "BTech")

p1 = PhDCandidate(
    "Ananya",
    27,
    "PhD Computer Science",
    "Artificial Intelligence in Healthcare Systems"
)
p1.display()
Student.count_students()
print(PhDCandidate.validate_thesis("Artificial Intelligence"))
print(PhDCandidate.validate_thesis("AI Thesis"))