from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, health, power):
        self.health = health
        self.power = power

    @abstractmethod
    def attack(self):
        pass


class Warrior(Character):
    def attack(self):
        return self.power * 2


class Archer(Character):
    def attack(self):
        return self.power * 1.5


if __name__ == "__main__":
    characters = [
        Warrior(100, 20),
        Archer(80, 15)
    ]

    for char in characters:
        print("Attack Power:", char.attack())
