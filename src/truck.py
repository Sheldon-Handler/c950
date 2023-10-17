"""
truck.py file to store Truck class.

Attributes:
    Status: Status Enum class to store status of truck delivery.
    Truck: Truck class to store truck information.
"""

# Import Enum from enum
from enum import Enum


# Status Enum class
class Status(Enum):
    """
    Status Enum class to store status of truck delivery.

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
class Truck:
    """
    Truck class to store truck information.

    Methods:
        __init__: Constructor for Truck class.
        __str__: String representation of Truck class.
    """

    # Constructor
    def __init__(self, truck_id: int, packages: list, status: Status):
        """
        Constructor for Truck class.

        Args:
            truck_id (): id of truck
            packages (): list of packages on truck
            status (): status of truck
        """

        # Set truck ID
        self.truck_id = truck_id

        # Set packages
        self.packages = packages

        # Set status
        self.status = status

    # String representation
    def __str__(self):
        """
        String representation of Truck class.

        Returns:
            String representation of Truck class.
        """

        # Return string representation of Truck class
        return f"Truck ID: {self.truck_id}\nPackages: {self.packages}\nStatus: {self.status}"
