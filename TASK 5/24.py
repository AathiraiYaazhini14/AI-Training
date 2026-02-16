from abc import ABC, abstractmethod

class PaymentSource(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


class BankAccount(PaymentSource):
    def process_payment(self, amount):
        return f"Paid {amount} using Bank Account"


class WalletBalance(PaymentSource):
    def process_payment(self, amount):
        return f"Paid {amount} using Wallet Balance"


if __name__ == "__main__":
    payments = [BankAccount(), WalletBalance()]
    for method in payments:
        print(method.process_payment(500))
