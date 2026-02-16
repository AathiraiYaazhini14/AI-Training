class vehicle:
    def __init__(self,brand,fuel):
        self.brand=brand
        self.fuel=fuel
    def behav(self):
        pass
class car(vehicle):
    def behav(self):
        print("Its a Car")
class bike(vehicle):
    def behav(self):
        print("Its a bike")
v1=car("BMW","Pet")
v2=bike("Duke","Dis")
v1.behav()
v2.behav()