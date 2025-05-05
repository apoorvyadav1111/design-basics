from enum import Enum
from uuid import uuid4
from datetime import datetime

from entities.book_item import BookItem
from entities.cd import CD
from entities.magazine import Magazine

__ITEM_TYPE_MAP = {
    "book": BookItem,
    "magazine": Magazine,
    "cd": CD
}

class ItemStatus(Enum):
    AVAILABLE = "available"
    CHECKED_OUT = "checked_out"

class Item:
    def __init__(self, title: str):
        self._id = str(uuid4())
        self.title = title
        self.status = ItemStatus.AVAILABLE
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def mark_checked_out(self):
        self.status = ItemStatus.CHECKED_OUT
        self.updated_at = datetime.now()

    def mark_available(self):
        self.status = ItemStatus.AVAILABLE
        self.updated_at = datetime.now()

    def __repr__(self):
        return f"{self.__class__.__name__}(id={self._id}, title={self.title}, status={self.status.value})"



class ItemFactory:
    @staticmethod
    def create_item(item_type: str, **kwargs):
        item_type = item_type.lower()

        if item_type == "book":
            return BookItem.build(**kwargs)
        elif item_type == "magazine":
            return Magazine.build(**kwargs)
        elif item_type == "cd":
            return CD.build(**kwargs)
        else:
            raise ValueError(f"Unknown item type: {item_type}")

