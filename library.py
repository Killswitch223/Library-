from book import Book
from user import User
from transaction import Transaction


class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.transactions = []

    def load_data(self):
        try:
            with open("books.txt", "r") as f:
                self.books = [Book.from_file(line) for line in f]
        except FileNotFoundError:
            pass

        try:
            with open("users.txt", "r") as f:
                self.users = [User.from_file(line) for line in f]
        except FileNotFoundError:
            pass

    def save_books(self):
        with open("books.txt", "w") as f:
            for book in self.books:
                f.write(book.to_file())

    def add_book(self, book):
        self.books.append(book)
        self.save_books()

    def view_books(self):
        for book in self.books:
            print(book.book_id, book.title, book.author, book.available)

    def borrow_book(self, user_id, book_id):
        for book in self.books:
            if book.book_id == book_id and book.available:
                book.borrow()
                self.transactions.append(Transaction(user_id, book_id))
                self.save_books()
                print("Book borrowed successfully")
                return
        print("Book not available")

    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                book.return_book()
                self.save_books()
                print("Book returned successfully")
                return
        print("Book not found")
