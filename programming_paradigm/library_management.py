class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__is_checked_out = False  # Books start as available by default

    def check_out(self):
        if not self.__is_checked_out:  # Check if the book is available
            self.__is_checked_out = True
            return True
        return False  # Already checked out

    def return_book(self):
        if self.__is_checked_out:  # Check if the book is checked out
            self.__is_checked_out = False
            return True
        return False  # Already available

    def is_checked_out(self):
        return self.__is_checked_out


class Library:
    def __init__(self):
        self.__books = []

    def add_book(self, book):
        if isinstance(book, Book):  # Ensure only Book objects are added
            self.__books.append(book)

    def check_out_book(self, title):
        for book in self.__books:
            if book.title == title:
                if book.check_out():
                    print(f"'{title}' has been checked out.")
                    return
                else:
                    print(f"'{title}' is already checked out.")
                    return
        print(f"'{title}' not found in the library.")

    def return_book(self, title):
        for book in self.__books:
            if book.title == title:
                if book.return_book():
                    print(f"'{title}' has been returned.")
                    return
                else:
                    print(f"'{title}' was not checked out.")
                    return
        print(f"'{title}' not found in the library.")

    def list_available_books(self):
        available_books = [book for book in self.__books if not book.is_checked_out()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books are currently available.")
