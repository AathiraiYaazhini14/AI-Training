from abc import ABC, abstractmethod

class SmartDevice(ABC):
    def __init__(self, device_id):
        self.device_id = device_id
        self.status = "OFF"

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class Light(SmartDevice):
    def turn_on(self):
        self.status = "Light ON"

    def turn_off(self):
        self.status = "Light OFF"


class Fan(SmartDevice):
    def turn_on(self):
        self.status = "Fan ON"

    def turn_off(self):
        self.status = "Fan OFF"


if __name__ == "__main__":
    devices = [Light(1), Fan(2)]
    for device in devices:
        device.turn_on()
        print(device.status)
        device.turn_off()
        print(device.status)
