class Shipment:
    def delivery_time(self):
        pass

class Air(Shipment):
    def delivery_time(self):
        return 2

class Ground(Shipment):
    def delivery_time(self):
        return 5

print(Air().delivery_time())
print(Ground().delivery_time())
