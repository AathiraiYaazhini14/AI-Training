class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            print(f"You borrowed '{self.title}'")
        else:
            print(f"'{self.title}' is currently not available")

    def return_book(self):
        if not self.available:
            self.available = True
            print(f"You returned '{self.title}'")
        else:
            print(f"'{self.title}' was not borrowed")

    def display(self):
        status = "Available" if self.available else "Not Available"
        print("Title:", self.title)
        print("Author:", self.author)
        print("Status:", status)



b1 = Book("The Alchemist", "Paulo Coelho")
b2 = Book("Atomic Habits", "James Clear")

b1.display()
b1.borrow()
b1.borrow()       
b1.return_book()
b1.display()
