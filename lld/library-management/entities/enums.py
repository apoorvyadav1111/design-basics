from enum import Enum

class MembershipStatus(Enum):
    """
    Enum representing the status of a membership.
    """
    ACTIVE = "active"
    INACTIVE = "inactive"
    SUSPENDED = "suspended"

class ItemStatus(Enum):
    """
    Enum representing the status of an item.
    """
    AVAILABLE = "available"
    CHECKED_OUT = "checked_out"