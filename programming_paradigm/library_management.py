class Book:
    def __init__(self,Title, Author):
        self.title = Title
        self.author = Author
        self._is_checked_out = True
    def check_out(self):
        self._is_checked_out = False
    def return_book(self):
        self._is_checked_out = True
    # def get__is_checked_out(self):
    #     return self._is_checked_out
class Library:
    def __init__(self):
        self._books  = []

    def add_book(self,book):
        self._books.append(book)
    
    def check_out_book(self,Title):
        for book in self._books:
            if book.title == Title:
                book.check_out()

    def return_book(self,Title):
        for book in self._books:
            if book.title == Title:
                book.return_book()

    def list_available_books(self):
        for book in self._books:
            if book._is_checked_out is True:
                print(f"{book.title} by {book.author}")
    