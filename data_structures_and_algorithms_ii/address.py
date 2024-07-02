class Address:
    """Represents an address object with its information."""

    def __init__(
        self,
        id: int,
        name: str,
        address: str,
        packages: [int] = [],
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
        self.packages = packages

    def __str__(self):
        """Returns the string representation of the Address object."""
        return f"ID: {self.id}, Name: {self.name}, Address: {self.address}, Packages: {self.packages}"

    def load_address(self, package_id: int) -> None:
        """Loads a package onto a truck.

        Args:
            package_id (int): The ID of the package.
            truck_id (int): The ID of the truck.

        Returns:
            bool: True if the address was loaded successfully. False if the address was not loaded successfully.
        """
        self.packages.append(package_id)
