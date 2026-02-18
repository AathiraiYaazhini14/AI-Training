from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car engine started")

    def stop(self):
        print("Car stopped")

class Bike(Vehicle):
    def start(self):
        print("Bike engine started")

    def stop(self):
        print("Bike stopped")

vehicles = [Car(), Bike()]
for v in vehicles:
    v.start()
    v.stop()
