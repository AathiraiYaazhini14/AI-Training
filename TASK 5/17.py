from abc import ABC, abstractmethod

class UtilityBill(ABC):
    def __init__(self, customer, units):
        self.customer = customer
        self.units = units

    @abstractmethod
    def calculate_bill(self):
        pass


class ElectricityBill(UtilityBill):
    def calculate_bill(self):
        return self.units * 7


class WaterBill(UtilityBill):
    def calculate_bill(self):
        return self.units * 3


if __name__ == "__main__":
    bills = [
        ElectricityBill("Alice", 100),
        WaterBill("Bob", 100)
    ]

    for bill in bills:
        print("Bill Amount:", bill.calculate_bill())
