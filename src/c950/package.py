"""package.py file to store Package class."""
from enum import Enum, global_enum

# Import dataclass from dataclasses
from dataclasses import dataclass


# Package dataclass
@dataclass(order=True, frozen=True)
class Package:
    """This Package dataclass is used to represent a package object to store
    package information.

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
        list_repr(): Return list representation of package.
        create_from_list(package_row): Create package from list.

    Example:
        package = Package(package_id, address, city, state, zip_code, weight, deadline, note, status)
        package.package_id  # Returns package_id
        package.address  # Returns address
        package.city  # Returns city
        package.state  # Returns state
        package.zip_code  # Returns zip_code
        package.weight  # Returns weight
        package.deadline  # Returns deadline
        package.note  # Returns note
        package.status  # Returns status

    References:
        https://docs.python.org/3/library/dataclasses.html?highlight=dataclass#dataclasses.dataclass
    """

    # Attribute package_id
    package_id: int
    # Attribute address
    address: str
    # Attribute city
    city: str
    # Attribute state
    state: str
    # Attribute zip_code
    zip_code: str
    # Attribute weight
    weight: int
    # Attribute deadline
    deadline: str
    # Attribute note
    note: str
    # Attribute status
    status: str

    def __hash__(self):
        return hash(self.package_id)

    # Method to return list representation of package.
    def to_list(self):
        """This method is used to get a List representation of the package
        object.

        Returns:
            list: List representation of package.

        References:
            https://docs.python.org/3/library/stdtypes.html#list
        """

        return [self.package_id, self.address, self.city, self.state, self.zip_code, self.weight, self.deadline,
                self.note, self.status]
