from typing import Optional
from services.item_service import ItemService
from services.member_service import MemberService
from services.ledger_service import LedgerService
from entities.enums import ItemStatus, MembershipStatus


class LibraryManagementService:
    def __init__(self, item_service: ItemService, member_service: MemberService, ledger_service: LedgerService):
        self.item_service = item_service
        self.member_service = member_service
        self.ledger_service = ledger_service

    def checkout_item(self, member_id: str, item_id: str, librarian_id: str) -> bool:
        member = self.member_service.get_member(member_id)
        item = self.item_service.get_item(item_id)

        if not member or not item:
            print("Invalid member or item ID.")
            return False

        if member.get_membership_status() != MembershipStatus.ACTIVE:
            print("Membership inactive.")
            return False

        if item.status != ItemStatus.AVAILABLE:
            print("Item not available.")
            return False

        self.item_service.update_status(item_id, ItemStatus.CHECKED_OUT)
        self.ledger_service.record_checkout(member_id, item_id, librarian_id)
        return True

    def return_item(self, member_id: str, item_id: str, librarian_id: str) -> bool:
        item = self.item_service.get_item(item_id)

        if not item:
            print("Invalid item ID.")
            return False

        self.item_service.update_status(item_id, ItemStatus.AVAILABLE)
        self.ledger_service.record_return(member_id, item_id, librarian_id)
        return True

    def add_item(self, item_object, librarian_id: str):
        """
        Add a new item to the library (book, magazine, CD, etc.)
        """
        self.item_service.add_item(item_object)
        # optionally log this via ledger or admin audit
        print(f"Item added by librarian {librarian_id}: {item_object}")

    def reserve_item(self, member_id: str, item_id: str) -> bool:
        """
        Future extension for reservation support
        """
        print("Reservation logic not yet implemented.")
        return False
