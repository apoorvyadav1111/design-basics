from person import Person
from uuid import uuid4

class Librarian(Person):
    def __init__(self, name: str, age: int, gender: str):
        super().__init__(name, age, gender)  # Inherit from Person
        self.employee_id = str(uuid4())  # Unique ID for the librarian (employee)
        self.assigned_books = []  # Track books assigned to the librarian

    def assign_book(self, book_item):
        """
        Assign a book item to the librarian's responsibility.
        """
        self.assigned_books.append(book_item)
    
    def __repr__(self):
        return f"Librarian(ID={self._id}, Name={self.name}, EmployeeID={self.employee_id}, AssignedBooks={len(self.assigned_books)})"
