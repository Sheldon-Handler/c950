#  MIT License
#
#  Copyright (c) 2023 Sheldon Handler
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice (including the next paragraph) shall be included in all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

from c950.model.address import Address
from c950 import addresses, distances


# Calculates the distance between two locations.
## time complexity: O(1)
## space complexity: O(1)
def get(
    location_a: Address or int,
    location_b: Address or int,
    distances: list[list] = distances,
    addresses: list[Address] = addresses,
) -> float:
    """
    Calculates the distance between two locations.

    Args:
        distance_matrix (list[list]): A two-dimensional list where each element represents
            the distance between two locations.

        location_a (Address): The first address to calculate the distance between.
        location_b (Address): The second address to calculate the distance between.
        distances (list[list]): A list of lists representing the distance matrix.
        addresses (list[Address]): A list of Address objects.

    Returns:
        float: The distance between the two locations.

    Notes:
        time complexity:
            best case = O(1)
            worst case = O(1)
            average case = O(1)
        space complexity:
            best case = O(1)
            worst case = O(1)
            average case = O(1)
    """

    # If location_a is an Address object
    if location_a is type(Address):
        # Get the index of location_a in the address_list
        location_a = addresses.index(location_a)
    elif location_a is type(int):
        location_a = location_a
    else:
        raise ValueError("location_a must be an object of type Address or int.")

    # If location_b is an Address object, convert it to the index of location_b in the address_list
    if location_b is type(Address):
        # Get the index of location_b in the address_list
        location_b = addresses.index(location_b)
    elif location_b is type(int):
        location_b = location_b
    else:
        raise ValueError("location_b must be an object of type Address or int.")

    # Distance between location_a and location_b in sublist of location_a
    location_grid_1 = distances[location_a][location_b]
    # Distance between location_a and location_b in sublist of location_b
    location_grid_2 = distances[location_b][location_a]

    # Find the distance between location_a and location_b. Find the distance_matrix for the distance between location_a
    # and location_b in the sublist of location_a and the sublist of location_b.
    if location_grid_1 is type(float):
        return location_grid_1
    elif location_grid_2 is type(float):
        return location_grid_2
    else:
        raise ValueError(
            "The distance between location_a and location_b is not in the distance_matrix."
        )
