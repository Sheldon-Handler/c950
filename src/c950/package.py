"""package.py file to store Package class."""
import dataclasses
from collections import namedtuple
from enum import Enum, global_enum

# Import dataclass from dataclasses
from dataclasses import dataclass


# Package namedtuple to store package information
Package = namedtuple(typename='Package', field_names=['package_id', 'address', 'city', 'state', 'zip_code', 'weight',
                                                      'deadline', 'note', 'status'])
Package.__doc__ = """This Package namedtuple is used to represent a package object to store package information."""
Package._fields = lambda package_id, address, city, state, zip_code, weight, deadline, note, status: (
    package_id, address, city, state, zip_code, weight, deadline, note, status)


class PackageList(list):
    """This PackageList class is used to represent a list of packages.

    Attributes:
        packages (list): list of packages

    Methods:
        __init__(packages): Initialize the PackageList instance.
        __add__(package): Add package to list.
        __delitem__(package): Remove package from list.
        __getitem__(package_id): Get package from list by package_id.
        get_all(): Get all packages from list.
        """

    def __init__(self):
        """Initialize the PackageList instance.

        Args:
            self (PackageList): The PackageList instance to initialize.

        References:
            https://docs.python.org/3/reference/datamodel.html
        """
        # Call super constructor
        super().__init__()

    # Method to add package to list
    def __add__(self, package: Package):
        """Add package to list.

            Args:
                self (PackageList): The PackageList instance to add to.
                package (Package): The package to add to the list.

            Returns:
                None

            References:
                https://docs.python.org/3/reference/datamodel.html
        """
        # Check if package with package_id is already in the list
        for package.package_id in self.packages:
            # If package with package_id is already in the list
            if package.package_id == package.package_id:
                # Raise ValueError
                raise ValueError(f"Package with package_id {package.package_id} already exists in the list.")
        # Append package to list
        self.append(package)

        # Method to remove package from list
    def __delitem__(self, package_id):
        """Remove package from list.

        Args:
            self (PackageList): The PackageList instance to remove from.
            package (Package): The package to remove from the list.

            Returns:
                None

            References:
                https://docs.python.org/3/reference/datamodel.html
        """
        # Iterate over packages in list
        for package in self.packages:
            # If package_id matches package.package_id
            if package.package_id == package_id:
                # Remove package from list
                self.remove(package)

        # Method to get package from list by package_id
    def __getitem__(self, package_id: int) -> Package:
        """Get package from list by package_id.

            Args:
                self (PackageList): The PackageList instance to get from.
                package_id (int): The package_id to get from the list.

            Returns:
                Package: The package with the specified package_id.

            References:
                https://docs.python.org/3/reference/datamodel.html
        """
        # Iterate over packages in list
        for package in self.packages:
            # If package_id matches package.package_id
            if package.package_id == package_id:
                # Return package
                return package

    # Method to get all packages from list
    def get_all(self) -> list[Package]:
        """Get all packages from list.

        Args:
            self (PackageList): The PackageList instance to get from.

        Returns:
            list: A list of all packages.

        References:
            https://docs.python.org/3/reference/datamodel.html
        """
        # Return all packages
        return self.packages

# class Package:
#     """This Package dataclass is used to represent a package object to store
#     package information.
#
#     Attributes:
#         package_id (int): id of package
#         address (str): address of package
#         city (str): city of package
#         state (str): state of package
#         zip_code (str): zip code of package
#         weight (int): weight of package
#         deadline (str): deadline of package
#         note (str): note of package
#         status (Status): status of package
#
#     Methods:
#         list_repr(): Return list representation of package.
#         create_from_list(package_row): Create package from list.
#
#     Example:
#         package = Package(package_id, address, city, state, zip_code, weight, deadline, note, status)
#         package.package_id  # Returns package_id
#         package.address  # Returns address
#         package.city  # Returns city
#         package.state  # Returns state
#         package.zip_code  # Returns zip_code
#         package.weight  # Returns weight
#         package.deadline  # Returns deadline
#         package.note  # Returns note
#         package.status  # Returns status
#
#     References:
#         https://docs.python.org/3/library/dataclasses.html?highlight=dataclass#dataclasses.dataclass
#     """
#
#     # Attribute package_id
#     package_id: int
#     # Attribute address
#     address: str
#     # Attribute city
#     city: str
#     # Attribute state
#     state: str
#     # Attribute zip_code
#     zip_code: str
#     # Attribute weight
#     weight: int
#     # Attribute deadline
#     deadline: str
#     # Attribute note
#     note: str
#     # Attribute status
#     status: str
#
#     def __init__(self, package_id: int, address: str, city: str, state: str, zip_code: str, weight: int, deadline: str, note: str, status: str):
#         self.package_id = package_id
#         self.address = address
#         self.city = city
#         self.state = state
#         self.zip_code = zip_code
#         self.weight = weight
#         self.deadline = deadline
#         self.note = note
#         self.status = status
#
#     def __repr__(self):
#
#
#     # Method to return list representation of package.
#     def to_list(self):
#         """This method is used to get a List representation of the package
#         object.
#
#         Returns:
#             list: List representation of package.
#
#         References:
#             https://docs.python.org/3/library/stdtypes.html#list
#         """
#
#         return [self.package_id, self.address, self.city, self.state, self.zip_code, self.weight, self.deadline,
#                 self.note, self.status]
