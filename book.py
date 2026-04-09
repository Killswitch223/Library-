class Book:
    def __init__(self, book_id, title, author, available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = available

    def borrow(self):
        self.available = False

    def return_book(self):
        self.available = True

    def to_file(self):
        return f"{self.book_id},{self.title},{self.author},{self.available}\n"

    @staticmethod
    def from_file(line):
        parts = line.strip().split(",")
        return Book(parts[0], parts[1], parts[2], parts[3] == "True")
