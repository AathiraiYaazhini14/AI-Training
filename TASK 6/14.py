import random

class Catalog:
    def __init__(self, items):
        self.items = items

    def random_item(self):
        return random.choice(self.items)

catalog = Catalog(["A", "B", "C", "D"])
print(catalog.random_item())
