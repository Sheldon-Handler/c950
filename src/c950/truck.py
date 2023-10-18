"""This Python module defines a Status Enum class to represent the status of
the truck, and a truck dataclass to store the truck information."""

# Import Enum from enum
from enum import Enum
# Import dataclass from dataclasses
from dataclasses import dataclass


# Status Enum class
class Status(Enum):
    """Status Enum class to store status of truck delivery.

    Attributes:
        AT_HUB: Enum constant for truck at hub
        EN_ROUTE: Enum constant for truck en route
        RETURNING: Enum constant for truck returning
        FINISHED: Enum constant for truck finished
    """

    # Set enum constant for truck at hub
    AT_HUB = (0, "At Hub")
    # Set enum constant for truck en route
    EN_ROUTE = (1, "En Route")
    # Set enum constant for truck returning
    RETURNING = (2, "Returning")
    # Set enum constant for truck finished
    FINISHED = (3, "Finished")


# Truck class
@dataclass
class Truck:
    """Truck dataclass to store truck information.

    Attributes:
        truck_id (int): ID of truck
        packages (list): packages on truck
        status (Status): status of truck
    """

    # ID of truck
    truck_id: int
    # Packages on truck
    packages: list
    # Status of truck
    status: Status
