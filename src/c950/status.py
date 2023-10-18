"""This module defines the enum classes for package status and truck status.

See Also:
    https://docs.python.org/3/library/enum.html
"""

# Import Enum from enum
from enum import Enum


# PackageStatus Enum class
class PackageStatus(Enum):
    """PackageStatus Enum class to store status of package.

    Attributes:
        UNDEFINED: Enum constant for package with undefined status
        NOT_AVAILABLE: Enum constant for package not available
        AT_HUB: Enum constant for package at hub
        EN_ROUTE: Enum constant for package en route
        DELIVERED: Enum constant for package delivered

    Usage:
        package_status = PackageStatus.NOT_AVAILABLE
        package_status.value  # Returns 0
        package_status.name  # Returns "NOT_AVAILABLE"

    References:
        https://docs.python.org/3/library/enum.html
    """

    __order__ = "NOT_AVAILABLE AT_HUB EN_ROUTE DELIVERED"
    # Set enum constant for package with undefined status
    UNDEFINED = None
    # Set enum constant for package not available
    NOT_AVAILABLE = 0
    # Set enum constant for package at hub
    AT_HUB = 1
    # Set enum constant for package en route
    EN_ROUTE = 2
    # Set enum constant for package delivered
    DELIVERED = 3


# TruckStatus Enum class
class TruckStatus(Enum):
    """TruckStatus Enum class to store status of truck.

    Attributes:
        UNDEFINED: Enum constant for truck with undefined status
        AT_HUB: Enum constant for truck at hub
        EN_ROUTE: Enum constant for truck en route
        RETURNING: Enum constant for truck returning
        FINISHED: Enum constant for truck finished

    Usage:
        truck_status = TruckStatus.AT_HUB
        truck_status.value  # Returns 0
        truck_status.name  # Returns "AT_HUB"

    References:
        https://docs.python.org/3/library/enum.html
    """

    # Set order of enum constants
    __order__ = "UNDEFINED AT_HUB EN_ROUTE RETURNING FINISHED"
    # Set enum constant for truck with undefined status
    UNDEFINED = ""
    # Set enum constant for truck at hub
    AT_HUB = "At Hub"
    # Set enum constant for truck en route
    EN_ROUTE = "En Route"
    # Set enum constant for truck returning
    RETURNING = "Returning"
    # Set enum constant for truck finished
    FINISHED = "Finished"
