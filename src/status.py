"""
status.py file to store Status Enum class to store status of package delivery.
:imports Enum: Enum to inherit from
:classes Status: Status Enum class to store status of package delivery.
"""

# Import Enum from enum
from enum import Enum


# Status Enum subclass of Enum to store status of package delivery
class Status(Enum):
    """
    Status Enum class to store status of package delivery.
    :super Enum: Enum to inherit from
    :constants: NOT_AVAILABLE, AT_HUB, EN_ROUTE, DELIVERED
    """

    # Enum constant for package not available
    NOT_AVAILABLE = (0, "Not Available")
    # Enum constant for package at hub
    AT_HUB = (1, "At Hub")
    # Enum constant for package en route
    EN_ROUTE = (2, "En Route")
    # Enum constant for package delivered
    DELIVERED = (3, "Delivered")
