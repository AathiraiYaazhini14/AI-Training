from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def salary(self):
        pass

class FullTime(Employee):
    def salary(self):
        return 50000

class Contract(Employee):
    def salary(self):
        return 30000

print(FullTime("A").salary())
print(Contract("B").salary())
