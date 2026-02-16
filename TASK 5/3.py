import math

class Shape:
    def area(self):
        pass  


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


# Menu Driven Program
while True:
    print("\n1. Rectangle")
    print("2. Circle")
    print("3. Triangle")
    print("4. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        l = float(input("Enter length: "))
        w = float(input("Enter width: "))
        r = Rectangle(l, w)
        print("Area:", r.area())

    elif ch == 2:
        r = float(input("Enter radius: "))
        c = Circle(r)
        print("Area:", c.area())

    elif ch == 3:
        b = float(input("Enter base: "))
        h = float(input("Enter height: "))
        t = Triangle(b, h)
        print("Area:", t.area())

    else:
        break
