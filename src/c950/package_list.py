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
        package_list (list): A list of Package objects.
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
            super().append(list(package))
            # Write PackageList to CSV file
            self.csvwriter.write(self)

    def find(self, package_id: int) -> list:
        """
        Args:
            package_id (int): The package_id of the Package to find.

        Returns:
            list: The Package object as a list with the given package_id.
        """

        # Iterate over packages in the list
        for package in self:
            # Check if package.package_id is equal to package_id
            if package.package_id == package_id:
                # Return package
                return package

    # Method to delete the Package with the given package_id from package_list
    def delete(self, package_id: int):
        """Delete a Package object with the given package_id from the
        package_list.

        Args:
            self (PackageList): The PackageList instance to delete from.
            package_id (str): The package_id of the Package object to delete.

        Returns:
            None
        """

        # Find the Package with the given package_id
        package_found = self.find(package_id)
        # Check if package_found is None
        if package_found == None:
            # Raise ValueError if package_found is None
            raise ValueError("Package not found.")
        # Otherwise
        else:
            # Remove package_found from the list
            super().remove(package_found)
            # Write PackageList to CSV file
            self.csvwriter.write(self)
