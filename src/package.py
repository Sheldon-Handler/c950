import collections
import dataclasses
from enum import Enum
import sqlite3
from dataclasses import dataclass, field


class Status(Enum):
    """
    Status Enum class to store status of package delivery.
    :param Enum: Enum to inherit from
    :type Enum: Enum
    """

    NOT_AVAILABLE = (0, "Not Available")
    AT_HUB = (1, "At Hub")
    EN_ROUTE = (2, "En Route")
    DELIVERED = (3, "Delivered")


# Dataclass decorator to store dataclass
@dataclass
class Package:
    """
    Package dataclass to store package information.
    :param dataclass: dataclass to inherit from
    :type dataclass: dataclass
    """

    # id of package
    package_id: int = field(default=None)
    # address for delivery of package
    address: str = field(default=None)
    # city for delivery of package
    city: str = field(default=None)
    # state for delivery of package
    state: str = field(default=None)
    # postal code for delivery of package
    postal: str = field(default=None)
    # weight of package
    weight: int = field(default=None)
    # deadline for delivery of package
    deadline: str = field(default=None)
    # special note for package
    note: str = field(default=None)
    # status of package delivery. Default is NOT_AVAILABLE
    status: Status = field(default=Status.NOT_AVAILABLE)

    # Constructor
    def __init__(self, package_id: int, address: str, city: str, state: str, postal: str, weight: int, deadline: str,
                 note: str, status: Status):
        """
        Initialize package with package_id, address, city, state, postal, weight, deadline, note, and status
        :param self: package to initialize
        :type self: Package
        :param package_id: id of package
        :type package_id: int
        :param address: address for delivering package
        :type address: str
        :param city: city for delivery of package
        :type city: str
        :param state: state for delivery of package
        :type state: str
        :param postal: postal code for delivery of package
        :type postal: str
        :param weight: weight of package
        :type weight: int
        :param deadline: deadline for delivery of package
        :type deadline: str
        :param note: special note for package
        :type note: str
        :param status: status of package delivery
        :type status: Status
        """

        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.postal = postal
        self.weight = weight
        self.deadline = deadline
        self.note = note
        self.status = status

    # Method to get string representation of package
    def __str__(self):
        """
        String representation of package
        :param self: package to get string representation of
        :type self: Package
        :return: string representation of package
        :rtype: str
        """
        return f"Package ID: {self.package_id}\n" \
               f"Address: {self.address}\n" \
               f"City: {self.city}\n" \
               f"State: {self.state}\n" \
               f"Postal: {self.postal}\n" \
               f"Weight: {self.weight}\n" \
               f"Deadline: {self.deadline}\n" \
               f"Note: {self.note}\n" \
               f"Status: {self.status.name}\n"
