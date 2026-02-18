class Book:
    def __init__(self, title, price):
        self.title = title
        self.__price = price

    def update_price(self, price):
        self.__price = price

    def get_price(self):
        return self.__price

b = Book("Python",500)
b.update_price(600)
print(b.get_price())
