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

import distance_between
import data_structures_and_algorithms_ii


# Nearest Neighbor Algorithm (Greedy Algorithm) - Finds the nearest location to the current location.
## time complexity: O(n)
## space complexity: O(1)
def nearest_neighbor_index(
    current_location_index,
    hub_location_index=0,
    distances=data_structures_and_algorithms_ii.global_variables.distances,
    visited_location_indices=data_structures_and_algorithms_ii.global_variables.visited_location_indices,
) -> int:
    """
    Finds the nearest location to the current location from a list of locations. The nearest location is the location
    with the shortest distance from the current location.

    Args:
        current_location_index (int): The index of the current location.
        distances (list[list]): A list of lists representing the distance matrix.
        visited_location_indices (list[int]): A list of indices representing the visited locations.
        hub_location_index (int): The index of the hub location. Defaults to 0.

    Returns:
        int: The index of the nearest location.

    Notes:
        linear search (for loop):
            time complexity:
                best case = O(1)
                worst case = O(n)
                average case = O(n)
            space complexity:
                best case = O(1)
                worst case = O(1)
                average case = O(1)
    """

    # Find the sublist for the current location distance matrix
    location_sublist = distances[current_location_index]

    # Initialize the nearest location index and distance. Default to the first location in the sublist
    nearest_location_index = 0
    # Initialize the nearest location distance. Default to the first location in the sublist.
    nearest_location_distance = float("inf")

    # Search for the nearest location (the location with the shortest distance)
    for i in location_sublist:  # O(n) - for loop
        # If the current_location_index, hub_location, visited_location_indices are not included when finding
        # the nearest location; and that the currently assigned nearest_location_distance is greater than the distance
        # to location i in the location_sublist.
        if (
            i != current_location_index
            and i != hub_location_index
            and i not in visited_location_indices
            and nearest_location_distance
            > distance_between.get(current_location_index, i)
        ):
            # Set nearest_location_distance to the distance to location i in the location_sublist
            nearest_location_distance = location_sublist[i]
            # Set nearest_location_index to the index of location i in the location_sublist
            nearest_location_index = i

    return nearest_location_index
