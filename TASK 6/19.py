class Delivery:
    def deliver(self):
        pass

class Bike(Delivery):
    def deliver(self):
        print("Bike Delivery")

class Drone(Delivery):
    def deliver(self):
        print("Drone Delivery")

def dispatch(d):
    d.deliver()

dispatch(Bike())
dispatch(Drone())
