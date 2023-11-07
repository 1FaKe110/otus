from typing import List

from src.repo.book import Book


class User:
    def __init__(self, name: str, gender: str, address: str, age: int, **kwargs):
        self.name = name
        self.gender = gender
        self.address = address
        self.age = age
        self.etc = kwargs
        self.books: List[Book] = []

    def __dict__(self):
        return dict(name=self.name,
                    gender=self.gender,
                    address=self.address,
                    age=self.age,
                    books=self.books)

    def as_dict(self):
        return self.__dict__()

    def add_book(self, book: Book):
        if not isinstance(book, Book):
            raise ValueError("Книга не является экземпляром класса [Book]")
        self.books.append(book.as_dict())

    def __repr__(self):
        return f'User[{self.name}]'

    def __str__(self):
        return self
