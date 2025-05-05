from person import Person
from enums import ItemStatus, MembershipStatus
from uuid import uuid4

class Member(Person):
    def __init__(self, name: str, age: int, gender: str):
        super().__init__(name, age, gender)
        self.membership_status = MembershipStatus.ACTIVE
        self.member_id = str(uuid4())  # Unique ID for each member
        self.borrowed_books = []  # Track borrowed books
        self.reserved_books = []  # Track reserved books

    def update_membership_status(self, status: MembershipStatus):
        """
        Update the membership status of the member.
        """
        if not isinstance(status, MembershipStatus):
            raise ValueError("Invalid membership status")
        self.membership_status = status

    def borrow_book(self, book_item):
        """
        Add a book to the borrowed list.
        """
        if book_item.status == ItemStatus.AVAILABLE:
            self.borrowed_books.append(book_item)
            book_item.update_status(ItemStatus.CHECKED_OUT)  # Mark as checked out
        else:
            raise ValueError("Book is not available for borrowing.")

    def reserve_book(self, book_item):
        """
        Add a book to the reserved list.
        """
        if book_item.status == ItemStatus.AVAILABLE:
            self.reserved_books.append(book_item)
        else:
            raise ValueError("Book is not available for reservation.")

    def __repr__(self):
        return f"Member(ID={self._id}, Name={self.name}, MembershipStatus={self.membership_status}, BorrowedBooks={len(self.borrowed_books)}, ReservedBooks={len(self.reserved_books)})"
