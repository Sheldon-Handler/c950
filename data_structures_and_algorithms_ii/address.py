import data_structures_and_algorithms_ii


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


def get_address_from_string(
    address_string: str, addresses: list = data_structures_and_algorithms_ii.addresses
) -> Address:
    """
    This function searches for an address in the list of Address objects.

    Args:
        address_string (str): The address string to search for.
        addresses (list): The list of Address objects.

    Returns:
        Address: The Address object instance.

    Notes:
        time complexity: O(n)
        space complexity: O(1)
    """
    # Search for the address in the list of Address objects
    for address in addresses:  # O(n) - for loop
        if address_string is address.address:
            # Return the address if found
            return address

    # Raise an error if the address is not found
    raise ValueError(f"Address {address_string} not found.")
