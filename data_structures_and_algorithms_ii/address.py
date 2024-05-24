import csv
import dataclasses
import os

import data_structures_and_algorithms_ii


@dataclasses.dataclass(frozen=True, order=True)
class Address:
    """This dataclass represents an address instance with its information.

    Attributes:
        id (int): The id of the location.
        name (str): The name of the location.
        address (str): The address.

    Returns:
        Address: An Address object instance.
    """

    id: int
    name: str
    address: str


def load_addresses(
    file: os.path.relpath = data_structures_and_algorithms_ii.address_csv_file,
) -> [Address]:
    """
    This function reads a csv file and returns a list of Address objects.

    Args:
        file (): The file to read from.

    Returns:
        list: A list of Address objects.

    Notes:
        time complexity: O(n^2)
        space complexity: O(n)
    """
    # Read the csv file
    csv_reader = csv.reader(file)
    # Store the rows in a list converted to Address objects
    addresses = [Address(int(row[0]), str(row[1]), str(row[2])) for row in csv_reader]
    return addresses


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
        if address.address == address_string:
            # Return the address if found
            return address

    # Raise an error if the address is not found
    raise ValueError(f"Address {address_string} not found.")
