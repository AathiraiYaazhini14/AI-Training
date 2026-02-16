class Student:
    def __init__(self,name,dept,cgpa,year):
        self.name=name
        self.dept=dept
        self.cgpa=cgpa
        self.year=year
    def eligible(self):
        return self.cgpa>=7.0 and self.year>=3
    def display(self):
        print(self.name)
        print(self.dept)
        print(self.cgpa)
        print(self.year)
        if self.eligible():
            print("Yes")
        else:
            print("No")
stu=Student("Arun","AIDS",8.2,4)
stu.display()
    