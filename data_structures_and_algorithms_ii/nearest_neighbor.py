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


def sorted_neighbors(distances_list: [float]) -> [int]:
    """
    Sorts a list and returns a list of indexes sorted by the corresponding value in ascending order.

    Args:
        distances_list: The list to be sorted.

    Returns:
        A list of indexes where the values are sorted from small to high.

    Notes:
        time complexity: O(n log n)
        space complexity: O(n)
    """
    # Create a list of tuples with the index and the value.
    items_tuples = [(i, distances_list[i]) for i in distances_list]  # O(n) - for loop

    # Sort the list of tuples by the value.
    items_tuples.sort(key=lambda x: x[1])  # O(n log n) - sort

    # List of the indices sorted by the value.
    sorted_indices = [i[0] for i in items_tuples]  # O(n) - for loop

    return sorted_indices


def sorted_unvisited_neighbors(
    distances_list: [float], visited_location_indices: [int]
) -> [int]:
    """
    Get the nearest unvisited neighbor from a given location.

    Args:
        distances_list ([float]): The list of distances from the current location to all other locations.
        visited_location_indices ([int]): A list of indices representing the visited locations.

    Returns:
        int or None: The index of the nearest unvisited neighbor. None if all locations have been visited.

    Notes:
        time complexity: O(n^2)
        space complexity: O(1)
    """
    unvisited_location_indices = []

    for i in sorted_neighbors(distances_list):  # O(n) - for loop
        if i not in visited_location_indices:  # O(n) - in operator
            unvisited_location_indices.append(i)

    return unvisited_location_indices
