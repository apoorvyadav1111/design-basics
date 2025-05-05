from entities.book import Book
from entities.item import Item


class BookItem(Item):
    def __init__(self, book: Book):
        super().__init__()
        if not isinstance(book, Book):
            raise ValueError("BookItem must be initialized with a valid Book.")
        self.book = book

    def __repr__(self):
        return f"BookItem(Book: {self.book.title}, ISBN: {self.book.isbn}, Status: {self.status})"

    @classmethod
    def build(cls, book: Book):
        """
        Factory method to create a BookItem from a Book instance.
        """
        return cls(book=book)
