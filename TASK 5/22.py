from abc import ABC, abstractmethod

class Package(ABC):
    def __init__(self, sender, receiver):
        self.sender = sender
        self.receiver = receiver

    @abstractmethod
    def update_status(self):
        pass


class StandardDelivery(Package):
    def update_status(self):
        return "In transit - ETA 5 days"


class ExpressDelivery(Package):
    def update_status(self):
        return "In transit - ETA 1 day"


if __name__ == "__main__":
    p1 = StandardDelivery("Alice", "Bob")
    p2 = ExpressDelivery("John", "Sara")

    print(p1.update_status())
    print(p2.update_status())
