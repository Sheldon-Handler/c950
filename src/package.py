import enum
import sqlite3.dbapi2
from dataclasses import dataclass


class Status(enum.Enum):
    """
    Status enum to store package status
    :param Enum: enum to inherit from
    :type Enum: Enum
    """

    NOT_AVAILABLE = 0
    AT_THE_HUB = 1
    EN_ROUTE = 2
    DELIVERED = 3


@dataclass
class Package:
    """
    Package class to store package information
    """

    package_id: int
    address: str
    city: str
    state: str
    postal: str
    weight: int
    deadline: str
    note: str
    status: Status

    # @staticmethod
    # def get_all_packages() -> list['Package']:
    #     """
    #     Get all packages
    #     :return: list of all packages
    #     :rtype: list[Package]
    #     """
    #     conn = sqlite3.connect(database="../data/database.db")
    #     cursor = conn.cursor()
    #     cursor.execute("SELECT * FROM package")
    #     packages = cursor.fetchall()
    #     package_list = list.__init__([])
    #     for package in packages:
    #         package_list.append(Package(package_id=package[0], address=package[1], city=package[2], state=package[3],
    #                                     postal=package[4], weight=package[5], deadline=package[6], note=package[7],
    #                                     status=Status(package[8])))
    #     return package_list
    #
    # @staticmethod
    # def get_package(package_id: int) -> 'Package':
    #     """
    #     Get package from package_id
    #     :param package_id: id of package to get
    #     :type package_id: int
    #     :return: package from package_id
    #     :rtype: Package
    #     """
    #     conn = sqlite3.connect(database="../data/database.db")
    #     cursor = conn.cursor()
    #     cursor.execute("SELECT * FROM package WHERE package_id = ?", [package_id])
    #     package = cursor.fetchone()
    #     return Package(package_id=package[0], address=package[1], city=package[2], state=package[3], postal=package[4],
    #                    weight=package[5], deadline=package[6], note=package[7], status=Status(package[8]))
    #
    # @staticmethod
    # def set_package(package_id: int, package: 'Package'):
    #     """
    #     Set package address
    #     :param package_id: id of package to set
    #     :type package_id: int
    #     :param package: package with correct data to set
    #     :type package: Package
    #     """
    #     conn = sqlite3.connect(database="../data/database.db")
    #     cursor = conn.cursor()
    #     cursor.execute("UPDATE package SET address = ? WHERE package_id = ?", [package, package_id])
    #     conn.commit()
    #
    # @staticmethod
    # def add_package(package: 'Package') -> 'Package':
    #     """
    #     Add package
    #     :param package: package to add
    #     :type package: Package
    #     :return: added package
    #     :rtype: Package
    #     """
    #     conn = sqlite3.connect(database="../data/database.db")
    #     cursor = conn.cursor()
    #     cursor.execute("INSERT INTO package (package_id, address, city, state, postal, weight, deadline, note, status) "
    #                    "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
    #                    [package.package_id, package.address, package.city, package.state, package.postal,
    #                     package.weight, package.deadline, package.note, package.status.value.__int__()])
    #     conn.commit()
    #     return package


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
    # def __setattr__(self, key, value):
    #     """
    #     Set attribute value
    #     :param self: package to set attribute value of
    #     :type self: Package
    #     :param key: attribute to set
    #     :type key: str
    #     :param value: value to set
    #     :type value: any
    #     """
    #     if key == "status":
    #         if value not in Status:
    #             raise ValueError(f"Invalid status: {value}")
    #     super().__setattr__(key, value)
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
