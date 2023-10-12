import collections
import dataclasses
import enum
import sqlite3
from dataclasses import dataclass, field


class Status(enum.Enum):
    """
    Status enum.Enum subclass to store package status.
    :param enum.Enum: enum class to inherit from
    :type enum.Enum: enum.Enum
    """

    NOT_AVAILABLE = 0
    NOT_AVAILABLE.name = "Not Available"

    AT_HUB = 1
    AT_HUB.name = "At Hub"

    EN_ROUTE = 2
    EN_ROUTE.name = "En Route"

    DELIVERED = 3
    DELIVERED.name = "Delivered"


@dataclass
class Package:
    """
    Package class to store package information
    """

    package_id: int = field(default=None)
    address: str = field(default=None)
    city: str = field(default=None)
    state: str = field(default=None)
    postal: str = field(default=None)
    weight: int = field(default=None)
    deadline: str = field(default=None)
    note: str = field(default=None)
    status: Status = field(default=None)

    # def __init__(self, package_id: int, address: str, city: str, state: str, postal: str, weight: int, deadline: str,
    #              note: str, status: Status):
    #     """
    #     Initialize package with package_id, address, city, state, postal, weight, deadline, note, and status
    #     :param self: package to initialize
    #     :type self: Package
    #     :param package_id: id of package
    #     :type package_id: int
    #     :param address: address for delivering package
    #     :type address: str
    #     :param city: city for delivery of package
    #     :type city: str
    #     :param state: state for delivery of package
    #     :type state: str
    #     :param postal: postal code for delivery of package
    #     :type postal: str
    #     :param weight: weight of package
    #     :type weight: int
    #     :param deadline: deadline for delivery of package
    #     :type deadline: str
    #     :param note: special note for package
    #     :type note: str
    #     :param status: status of package delivery
    #     :type status: Status
    #     """
    #
    #     self.package_id = package_id
    #     self.address = address
    #     self.city = city
    #     self.state = state
    #     self.postal = postal
    #     self.weight = weight
    #     self.deadline = deadline
    #     self.note = note
    #     self.status = status
    #
    # def __str__(self):
    #     """
    #     String representation of package
    #     :param: self: package to get string representation of
    #     :type self: Package
    #     :return: string representation of package
    #     :rtype: str
    #     """
    #     return (f"Delivery Package - Address: {self.address}, City: {self.city}, State: {self.state}, "
    #             f"Postal: {self.postal}, Weight: {self.weight}, Deadline: {self.deadline}, Note: {self.note}, "
    #             f"Status: {self.status}")
