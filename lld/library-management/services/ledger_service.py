from entities.transaction_record import TransactionRecord
from datetime import datetime
from collections import defaultdict

class LedgerService:
    def __init__(self):
        # Initialize your data structures here, e.g., logs or database connections
        self.transactions = defaultdict(list)  # A dictionary to hold transactions by member ID
        self.history = defaultdict(list)
    def record_checkout(self, member_id: str, item_id: str, librarian_id: str):
        """
        Log the checkout of an item by a member, performed by a librarian.
        """
        transaction = TransactionRecord(
            member_id=member_id,
            item_id=item_id,
            librarian_id=librarian_id
        )

        self.transactions[member_id].append(transaction)

    def record_return(self, member_id: str, item_id: str, librarian_id: str):
        """
        Log the return of an item by a member, handled by a librarian.
        """
        for transaction in self.transactions[member_id]:
            if transaction.item_id == item_id and not transaction.is_returned():
                transaction.update_return_date(datetime.now())
                self.history[member_id].append(transaction)
                self.transactions[member_id].remove(transaction)
                break
        else:
            raise ValueError(f"No active transaction found for item {item_id} by member {member_id}")


    def get_borrowed_items_by_member(self, member_id: str):
        """
        Retrieve all currently borrowed items for a specific member.
        """
        borrowed_items = []
        for transaction in self.transactions[member_id]:
            if not transaction.is_returned():
                borrowed_items.append(transaction.item_id)
        return borrowed_items

    def get_checkout_history_for_item(self, item_id: str):
        """
        Retrieve the full checkout/return history for a given item.
        """
        history = []
        for member_transactions in self.transactions.values():
            for transaction in member_transactions:
                if transaction.item_id == item_id:
                    history.append(transaction)
        return history
    

    def get_librarian_activity(self, librarian_id: str):
        """
        Retrieve the log of checkouts and returns handled by a specific librarian.
        """
        pass

    def get_overdue_items(self, current_date):
        """
        Identify all items that are overdue based on a given date.
        """
        pass
