from abc import ABC, abstractmethod

class DrivingMode(ABC):
    @abstractmethod
    def control_vehicle(self):
        pass


class EcoMode(DrivingMode):
    def control_vehicle(self):
        return "Driving in Eco mode"


class SportMode(DrivingMode):
    def control_vehicle(self):
        return "Driving in Sport mode"


if __name__ == "__main__":
    modes = [EcoMode(), SportMode()]
    for mode in modes:
        print(mode.control_vehicle())
