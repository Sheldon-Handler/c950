"""
package.py file to store Package class.
"""

# Import Enum from enum
from enum import Enum


# Status Enum class
class Status(Enum):
    """
    Status Enum class to store status of package delivery.

    Attributes:
        NOT_AVAILABLE: Enum constant for package not available
        AT_HUB: Enum constant for package at hub
        EN_ROUTE: Enum constant for package en route
        DELIVERED: Enum constant for package delivered
    """
    NOT_AVAILABLE = (0, "Not Available")
    AT_HUB = (1, "At Hub")
    EN_ROUTE = (2, "En Route")
    DELIVERED = (3, "Delivered")


# Package class
class Package:
    """
    Package class to store package information.

    Attributes:
        package_id (int): id of package
        address (str): address of package
        city (str): city of package
        state (str): state of package
        zip_code (str): zip code of package
        weight (int): weight of package
        deadline (str): deadline of package
        note (str): note of package
        status (Status): status of package

    Methods:
        __init__(package_id, address, city, state, zip_code, weight, deadline, note, status): Constructor for Package class.
        __str__(): String representation of Package class.
    """

    # Constructor
    def __init__(self, package_id: int, address: str, city: str, state: str, zip_code: str, weight: int, deadline: str, note: str, status: Status):
        """
        Constructor for Package class.

        Args:
            package_id (): id of package
            address (): address of package
            city (): city of package
            state (): state of package
            zip_code (): zip code of package
            weight (): weight of package
            deadline (): deadline of package
            note (): note of package
            status (): status of package
        """

        # Set package ID
        self.package_id = package_id

        # Set address
        self.address = address

        # Set city
        self.city = city

        # Set state
        self.state = state

        # Set zip code
        self.zip_code = zip_code

        # Set weight
        self.weight = weight

        # Set deadline
        self.deadline = deadline

        # Set note
        self.note = note

        # String representation
        def __str__(self):
            """
            String representation of Package class.
            :param: self: Package
            :type: self: Package
            :return: str
            """

            return f'Package ID: {self.package_id}, Address: {self.address}, City: {self.city}, State: {self.state}, Zip Code: {self.zip_code}, Weight: {self.weight}, Deadline: {self.deadline}, Note: {self.note}'
