from abc import ABC, abstractmethod

class Plan(ABC):
    @abstractmethod
    def bill_amount(self):
        pass

    @abstractmethod
    def validity_days(self):
        pass


class BasicPlan(Plan):
    def bill_amount(self):
        return 299

    def validity_days(self):
        return 30


class PremiumPlan(Plan):
    def bill_amount(self):
        return 2999

    def validity_days(self):
        return 365


if __name__ == "__main__":
    plans = [BasicPlan(), PremiumPlan()]
    for plan in plans:
        print("Bill:", plan.bill_amount(), "Validity:", plan.validity_days(), "days")
