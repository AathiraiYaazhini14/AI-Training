from abc import ABC, abstractmethod

class Ticket(ABC):
    def __init__(self, source, destination, distance):
        self.source = source
        self.destination = destination
        self.distance = distance

    @abstractmethod
    def calculate_fare(self):
        pass


class BusTicket(Ticket):
    def calculate_fare(self):
        return self.distance * 5


class TrainTicket(Ticket):
    def calculate_fare(self):
        return self.distance * 8


if __name__ == "__main__":
    tickets = [
        BusTicket("A", "B", 100),
        TrainTicket("A", "B", 100)
    ]

    for ticket in tickets:
        print("Fare:", ticket.calculate_fare())
