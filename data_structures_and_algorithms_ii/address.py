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
        """
        self.packages.append(package_id)


def load_from_package_list(addresses: [], packages: []) -> None:
    """Loads the addresses with their respective packages.

    Args:
        addresses ([]): The list of addresses.
        packages ([]): The list of packages.

    Returns:
        None
    """
    for i in addresses:
        for j in packages:
            if i.id == j.address:
                i.load_address(j.id)
                print(f"Package {j.id} loaded to address {i.id}.")
