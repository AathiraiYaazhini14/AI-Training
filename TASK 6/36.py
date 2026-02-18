class Enemy:
    def attack(self):
        pass

class Zombie(Enemy):
    def attack(self):
        print("Bite")

class Alien(Enemy):
    def attack(self):
        print("Laser")

for e in [Zombie(), Alien()]:
    e.attack()
