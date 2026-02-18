class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def study(self):
        print(f"{self.name} is studying")

class Teacher(Person):
    def teach(self):
        print(f"{self.name} is teaching")

s = Student("Alice", 16)
t = Teacher("Bob", 35)
s.study()
t.teach()
