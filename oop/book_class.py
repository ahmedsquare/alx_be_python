class Book:
    def __init__(self, title, author, year):
        __title__ = title
        __author__ = author
        __year__ = year
    
    def __del__(self):
        print(f"Deleting {self.__title__}")

    def __str__(self):
        return f"{self.__title__} by {self.__author__} published in {self.__year__}"
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"