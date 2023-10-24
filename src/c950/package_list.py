"""Module for Package namedtuple and PackageList class."""

#  MIT License
#
#  Copyright (c) 2023 Sheldon Handler
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice (including the next paragraph) shall be included in all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# Import csv_handler
import csv_handler

# Import Package from package
from package import Package


# PackageList class
class PackageList(list):
    """A list of Package objects.

    Attributes:
        csvwriter (CsvHandler): A CsvHandler instance for package.csv.

    See Also:
        https://docs.python.org/3/tutorial/datastructures.html
    """

    def __init__(self):
        """Initialize the PackageList instance.

        Args:
            self (PackageList): The PackageList instance to initialize.

        Returns:
            PackageList: A PackageList instance.
        """
        # Initialize the list
        super().__init__()
        # Create CsvHandler instance for package.csv
        self.csvwriter = csv_handler.CsvHandler(
            filename="../resources/package.csv",
            header=[
                "Package ID",
                "Address",
                "City",
                "State",
                "Zip",
                "Weight",
                "Delivery Deadline",
                "Special Notes",
                "Status",
            ],
        )

    def get_package(self, package_id: int) -> Package:
        """Method to retrieve a Package by package_id from PackageList.

        Args:
            self (PackageList): The PackageList instance to search.
            package_id (int): The package_id of the item to search for.

        Returns:
            Package: The Package with the given package_id.
        """

        for package in self:
            if package.package_id == package_id:
                return package
        raise KeyError("Package with package_id not found.")

    def get_index(self, package_id: int) -> int:
        """Method to retrieve the index of a Package by package_id from
        PackageList.

        Args:
            self (PackageList): The PackageList instance to search.
            package_id (int): The package_id of the item to search for.

        Returns:
            int: The index of the Package with the given package_id.
        """
        for package in self:
            if package.package_id == package_id:
                return self.index(package)
        raise KeyError("Package with package_id not found.")

    def append(self, package: Package):
        """Append a Package object to the package_list if a Package object with
        the same package_id is not already in the package_list.

        Args:
            self (PackageList): The PackageList instance to append to.
            package (Package): The Package object to append.

        Returns:
            None
        """

        # Check if package is of type Package
        if not isinstance(package, Package):
            # Raise TypeError if package is not of type Package
            raise TypeError("package must be of type Package.")
        # Check if the list contains a Package with the same package_id
        elif package.package_id in self:
            # Raise ValueError if the list contains a Package with the same package_id
            raise ValueError("Package with package_id already exists.")
        # Otherwise
        else:
            # Append package to the list
            super().append(package)
            # Write PackageList to CSV file
            self.csvwriter.write(self)

    # Method to delete the Package with the given package_id from package_list
    def delete(self, package_id: int) -> None:
        """Delete a Package object with the given package_id from the
        PackageList.

        Args:
            self (PackageList): The PackageList instance to delete from.
            package_id (int): The package_id of the Package object to delete.

        Returns:
            None
        """
        # Delete the Package with the given package_id
        del self[self.get_index(package_id)]

    # Method to update the Package with the given package_id in package_list
    def update(self, package: Package):
        """Update a Package object with the given package_id in the
        package_list.

        Args:
            package_id (int): id of the package to update
            package (Package): the package with the updated information

        Returns:
            None
        """

        # Get the index of the Package with the given package_id
        index = self.get_index(package.package_id)
        # Check if index is not None
        if index is not None:
            # Update the Package at the given index
            self[index] = package
            # Write PackageList to CSV file
            self.csvwriter.write(self)
