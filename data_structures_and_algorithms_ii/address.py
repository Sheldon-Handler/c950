import dataclasses
import csv
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


def get_addresses(file) -> data_structures_and_algorithms_ii.hash_table.HashTable:
    """
    This function reads a csv file and returns a list of Location objects.

    Args:
        file (): The file to read from.

    Returns:
        list: A list of Location objects.

    Notes:
        time complexity: O(n^2)
        space complexity: O(n)
    """
    address_table = data_structures_and_algorithms_ii.hash_table.HashTable()
    addresses = []

    csv_file = open(file, mode="r", newline="")
    reader = csv.reader(csv_file)

    # Parse the csv file and create a hash table of Address objects
    for row in reader:  # O(n) - for loop
        addresses.append(data_structures_and_algorithms_ii.address.Address(*row))
        address_table.set(
            row[1], data_structures_and_algorithms_ii.address.Address(*row)
        )  # O(n) - set

    csv_file.close()

    return address_table
