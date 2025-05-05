from entities.book import Book


class BookService:
    def __init__(self):
        self.books = {}

    def add_book(self, book: Book):
        """
        Add a book to the repository. If the book already exists, raise an error.
        """
        if book.isbn in self.books:
            raise ValueError(f"Book with ISBN {book.isbn} already exists.")
        self.books[book.isbn] = book

    def get_book(self, isbn: str) -> Book:
        """
        Retrieve a book by its ISBN.
        """
        return self.books.get(isbn)

    def remove_book(self, isbn: str):
        """
        Remove a book from the repository by its ISBN.
        """
        if isbn in self.books:
            del self.books[isbn]
        else:
            raise ValueError("Book not found.")
    
    def get_all_books(self):
        """
        Retrieve all books in the repository.
        """
        return list(self.books.values())
