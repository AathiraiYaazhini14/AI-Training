from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass

class PayPal(Payment):
    def pay(self):
        print("PayPal Payment")

class Stripe(Payment):
    def pay(self):
        print("Stripe Payment")

for p in [PayPal(), Stripe()]:
    p.pay()
