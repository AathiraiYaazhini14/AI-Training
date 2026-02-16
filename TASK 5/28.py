from abc import ABC, abstractmethod

class Sensor(ABC):
    @abstractmethod
    def interpret_data(self, raw_value):
        pass


class TemperatureSensor(Sensor):
    def interpret_data(self, raw_value):
        return raw_value * 0.1


class HumiditySensor(Sensor):
    def interpret_data(self, raw_value):
        return raw_value * 0.2


if __name__ == "__main__":
    sensors = [TemperatureSensor(), HumiditySensor()]
    for sensor in sensors:
        print(sensor.interpret_data(50))
