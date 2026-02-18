from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CardPayment(Payment):
    def pay(self, amount):
        print(f"Paid ${amount} using Card")

class UPIPayment(Payment):
    def pay(self, amount):
        print(f"Paid ${amount} using UPI")

def checkout(payment_method, amount):
    payment_method.pay(amount)

checkout(CardPayment(), 100)
checkout(UPIPayment(), 50)
