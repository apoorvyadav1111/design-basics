from datetime import datetime

class TransactionRecord:
    def __init__(self, member_id: str, item_id: str, librarian_id: str, checkout_date: datetime = None, return_date: datetime = None):
        """
        Initialize a transaction record to track checkout and return dates.

        :param member_id: The ID of the member involved in the transaction
        :param item_id: The ID of the item involved in the transaction
        :param librarian_id: The ID of the librarian handling the transaction
        :param checkout_date: The date when the item was checked out
        :param return_date: The date when the item was returned (if applicable)
        """
        self.member_id = member_id
        self.item_id = item_id
        self.librarian_id = librarian_id
        self.checkout_date = checkout_date or datetime.now()  # Default to the current time if not specified
        self.return_date = return_date

    def __repr__(self):
        """
        Return a string representation of the transaction record.
        """
        return (f"TransactionRecord(member_id={self.member_id}, item_id={self.item_id}, "
                f"librarian_id={self.librarian_id}, checkout_date={self.checkout_date}, return_date={self.return_date})")

    def is_returned(self) -> bool:
        """
        Check if the item has been returned.
        """
        return self.return_date is not None

    def update_return_date(self, return_date: datetime):
        """
        Update the return date for the item.
        """
        self.return_date = return_date
