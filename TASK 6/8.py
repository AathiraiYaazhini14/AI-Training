from abc import ABC, abstractmethod
class Attackstrat(ABC):
    @abstractmethod
    def attack(self):
        pass
class Sword(Attackstrat):
    def attack(self):
        print("Sword attack!")
class Bow(Attackstrat):
    def attack(self):
        print("Bow attack!")
class Charc:
    def __init__(self,name,strat:Attackstrat):
        self.name=name
        self._strat=strat
    def attack(self):
        print(f"{self.name}:",end=" ")
        self._strat.attack()
    def set_strat(self,strat:Attackstrat):
        self._strat=strat

characters = [
    Charc("Knight", Sword()),
    Charc("Archer", Bow()),
]

for character in characters:
    character.attack()