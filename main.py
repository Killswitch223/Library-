from library import Library
from book import Book


def main():
    library = Library()
    library.load_data()

    while True:
        print("\n1. Add Book")
        print("2. View Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            book_id = input("Enter ID: ")
            title = input("Enter title: ")
            author = input("Enter author: ")
            library.add_book(Book(book_id, title, author))

        elif choice == "2":
            library.view_books()

        elif choice == "3":
            user_id = input("Enter user ID: ")
            book_id = input("Enter book ID: ")
            library.borrow_book(user_id, book_id)

        elif choice == "4":
            book_id = input("Enter book ID: ")
            library.return_book(book_id)

        elif choice == "5":
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
