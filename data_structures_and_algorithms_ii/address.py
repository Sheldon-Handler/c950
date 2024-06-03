class Address:
    """Represents an address object with its information."""

    def __init__(self, id: int, name: str, address: str):
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

    def __str__(self):
        """Returns the string representation of the Address object."""
        return f"ID: {self.id}, Name: {self.name}, Address: {self.address}"
