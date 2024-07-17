#  MIT License
#
#  Copyright (c) 2024 Sheldon Handler
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice (including the next paragraph) shall be included in all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import package


class Address:
    """Represents an address object with its information."""

    def __init__(
            self,
            id: int,
            name: str,
            address: str,
    ):
        """
        Initializes an Address object instance with its information.

        Args:
            id (int): The id of the location.
            name (str): The name of the location.
            address (str): The address.
        """

        self.id = id
        self.name = name
        self.address = address
        self.packages = []

    def __str__(self):
        """Returns the string representation of the Address object."""
        return f"ID: {self.id}, Name: {self.name}, Address: {self.address}, Packages: {self.packages}"

    def load_address(self, package_id: int) -> None:
        """Loads a package onto a truck.

        Args:
            package_id (int): The ID of the package.

        Returns:
            bool: True if the address was loaded successfully. False if the address was not loaded successfully.

        Notes:
            time complexity:
                best case: O(1)
                worst case: O(1)
                average case: O(1)
            space complexity:
                best case: O(1)
                worst case: O(1)
                average case: O(1)
        """
        self.packages.append(package_id)


def load_from_package_list(
        addresses: [Address], packages: [package.Package]
) -> None:
    """Loads the addresses with their respective packages.

    Args:
        addresses ([address.Address]): The list of addresses.
        packages ([package.Package]): The list of packages.

    Returns:
        None
    """
    for i in addresses:  # O(n) - for loop
        for j in packages:  # O(n) - for loop
            if i.id == j.address_id:
                i.load_address(j.id)
                print(f"Package {j.id} loaded to address {i.id}.")
