from abc import ABC, abstractmethod

class Reservation(ABC):
    @abstractmethod
    def check_availability(self):
        pass


class NormalReservation(Reservation):
    def check_availability(self):
        return "Table available if not booked"


class VIPReservation(Reservation):
    def check_availability(self):
        return "VIP table reserved"


if __name__ == "__main__":
    reservations = [NormalReservation(), VIPReservation()]
    for r in reservations:
        print(r.check_availability())
