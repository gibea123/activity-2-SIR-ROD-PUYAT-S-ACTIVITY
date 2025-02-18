class Book:
    def __init__(self, title, author, year_published):
        self.title, self.author, self.year_published = title, author, year_published

    def describe(self):
        print(f"Title: {self.title}, Author: {self.author}, Year: {self.year_published}")

book1 = Book("1962", "A wrinkle in time", 1962)
book2 = Book("Winnie-the-pooh", "milne", 1926)
book3 = Book("The secret Garden", "Frances hodgson burnett", 1911)

book1.describe()
book2.describe()
book3.describe()