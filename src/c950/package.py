"""package.py file to store Package class."""

# Import dataclass from dataclasses
from dataclasses import dataclass
# Import Enum from enum
from enum import Enum


# Status Enum class
class Status(Enum):
    """This status Enum class is used to define an enum to represent the status
    of a package.

    Attributes:
        __order__ (str): The order of the enum constants.
        NOT_AVAILABLE: Enum constant for package not available.
        AT_HUB: Enum constant for package at hub.
        EN_ROUTE: Enum constant for package en route.
        DELIVERED: Enum constant for package delivered.

    References:
        https://docs.python.org/3/library/enum.html
    """

    # Set order of enum constants
    __order__ = "NOT_AVAILABLE AT_HUB EN_ROUTE DELIVERED"
    # Set enum constant for package not available
    NOT_AVAILABLE = (0, "Not Available")
    # Set enum constant for package at hub
    AT_HUB = (1, "At Hub")
    # Set enum constant for package en route
    EN_ROUTE = (2, "En Route")
    # Set enum constant for package delivered
    DELIVERED = (3, "Delivered")


# Package dataclass
@dataclass
class Package:
    """This Package dataclass is used to define a package and its attributes.

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

    References:
        https://docs.python.org/3/library/dataclasses.html
    """

    # Define dataclass attribute package_id as int
    package_id: int
    # Define dataclass attribute address as str
    address: str
    # Define dataclass attribute city as str
    city: str
    # Define dataclass attribute state as str
    state: str
    # Define dataclass attribute zip_code as str
    zip_code: str
    # Define dataclass attribute weight as int
    weight: int
    # Define dataclass attribute deadline as str
    deadline: str
    # Define dataclass attribute note as str
    note: str
    # Define dataclass attribute status as Status
    status: Status

    @classmethod
    def row(self):
        return [self.package_id, self.address, self.city, self.state, self.zip_code, self.weight, self.deadline,
                self.note, self.status.value]
