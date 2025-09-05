from models.book import Book
from abc import ABC, abstractmethod


class User(ABC):
    name: str
    borrowed_books: list[Book]

    @abstractmethod
    def get_user_info(self) -> str:
        pass

    @abstractmethod
    def borrow_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def return_book(self, book: Book) -> None:
        pass


class Member(User):
    def __init__(self, name) -> str:
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book: Book) -> None:
        self.borrowed_books.append(Book)

    def return_book(self, book: Book) -> None:
        self.borrowed_books.remove(Book)


class Librarian(User):
    def __init__(self, name) -> str:
        self.name = name

    def get_user_info(self, name) -> str:
        return f"Librarian : {self.name}"
