from abc import ABC, abstractmethod

class FoodItem(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @abstractmethod
    def final_price(self):
        pass


class VegFood(FoodItem):
    def final_price(self):
        return self.price * 1.05


class NonVegFood(FoodItem):
    def final_price(self):
        return self.price * 1.15


if __name__ == "__main__":
    items = [
        VegFood("Salad", 100),
        NonVegFood("Chicken", 200)
    ]

    for item in items:
        print(item.name, "Final Price:", item.final_price())
