from abc import ABC, abstractmethod

class Ride(ABC):
    def __init__(self, pickup, drop, distance):
        self.pickup = pickup
        self.drop = drop
        self.distance = distance

    @abstractmethod
    def fare(self):
        pass


class EconomyRide(Ride):
    def fare(self):
        return self.distance * 10


class PremiumRide(Ride):
    def fare(self):
        return self.distance * 20


if __name__ == "__main__":
    rides = [
        EconomyRide("A", "B", 10),
        PremiumRide("A", "B", 10)
    ]

    for ride in rides:
        print("Fare:", ride.fare())
