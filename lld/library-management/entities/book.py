from uuid import uuid4
from datetime import datetime

class Book:
    def __init__(self, title: str, author: str, publication_year: int, isbn: str):
        self.book_id = str(uuid4())
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.isbn = isbn
        self.created_at = datetime.now()

    def __str__(self):
        return f"Book(title={self.title}, author={self.author}, year={self.publication_year}, isbn={self.isbn})"
