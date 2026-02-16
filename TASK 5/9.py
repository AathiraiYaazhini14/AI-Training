class Course:
    def __init__(self,name):
        self.name=name
class Student:
    def __init__(self,name):
        self.name=name
        self.reg=set()
    def regi(self,course:Course):
        if course.name not in self.reg:
            self.reg.add(course.name)
c1=Course("Math")
c2=Course("Physics")
s=Student("Alice")
s.regi(c1)
s.regi