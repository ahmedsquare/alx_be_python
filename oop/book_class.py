class Book:
    def __init__(self, title, author, year):
        _title_ = title
        _author_ = author
        _year_ = year
    
    def __del__(self):
        print(f"Deleting {self._title_}")

    def __str__(self):
        return f"{self._title_} by {self._author_} published in {self._year_}"
    
    def __repr__(self):
        return f"Book('{self._title_}', '{self._author_}', {self._year_})"