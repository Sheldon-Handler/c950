#  MIT License
#
#  Copyright (c) 2024 Sheldon Handler
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice (including the next paragraph) shall be included in all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

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
