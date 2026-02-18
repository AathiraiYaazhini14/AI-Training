from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started with key")

class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started with kick")

for v in [Car(), Bike()]:
    v.start_engine()
