class Employee:
    def __init__(self, name, basic):
        self.name = name
        self.basic = basic

    def calculate_salary(self):
        pass


class Manager(Employee):
    def calculate_salary(self):
        return self.basic + (0.30 * self.basic)


class Developer(Employee):
    def calculate_salary(self):
        return self.basic + (0.20 * self.basic)


class Clerk(Employee):
    def calculate_salary(self):
        return self.basic + (0.10 * self.basic)


emp1 = Manager("Arun", 50000)
emp2 = Developer("Divya", 40000)
emp3 = Clerk("Rahul", 30000)

print(emp1.name, "Final Salary:", emp1.calculate_salary())
print(emp2.name, "Final Salary:", emp2.calculate_salary())
print(emp3.name, "Final Salary:", emp3.calculate_salary())
