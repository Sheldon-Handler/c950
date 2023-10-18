"""package.py file to store Package class."""
# Import dataclass from dataclasses
from dataclasses import dataclass
# Import PackageStatus from status
from status import PackageStatus


# Package dataclass
@dataclass(order=True)
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
        https://docs.python.org/3/library/dataclasses.html
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
    status: PackageStatus

    # Method to return list representation of package.
    def list_repr(self):
        """This method is used to get a List representation of the package
        object.

        Returns:
            list: List representation of package.

        See Also:
            https://docs.python.org/3/library/list.html
        """

        return [self.package_id, self.address, self.city, self.state, self.zip_code, self.weight, self.deadline, self.note, self.status]

    @classmethod
    def create_from_list(list):
        """This method is used to create a Package object from a list.

        Args:
            list (list): List of package attributes.

        Returns:
            Package: Package object.

        See Also:
            https://docs.python.org/3/library/list.html
        """

        return Package(list[0], list[1], list[2], list[3], list[4], list[5], list[6], list[7], PackageStatus(list[8]))
