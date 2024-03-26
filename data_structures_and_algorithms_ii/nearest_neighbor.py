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


def neighbors_sorted_by_distance_from_current_location(current_row: [float]) -> list:
    """
    Get the nearest neighbors from a given location. Sort by distance from the current location.

    Args:
        current_row (float): The list of distances from the current location to all other locations.

    Returns:
        list: A list of the location indices sorted by distance from the current location.

    Notes:
        time complexity: O(n log n)
        space complexity: O(n)
    """
    neighbors = []

    # Create a list of tuples with the location index and the distance from the current location
    for i in current_row: # O(n) - for loop
        neighbors.append((i, current_row[i]))

    # Sort the list of tuples by the distance from the current location
    neighbors.sort(key=lambda x: x[1]) # O(n log n) - sort

    # Return a list of the location indices sorted by distance from the current location
    indices_sorted_by_distance = [i[0] for i in neighbors] # O(n) - for loop

    return indices_sorted_by_distance


def nearest_unvisited_neighbor(current_row: [float], visited_location_indices: [int]) -> int or None:
    """
    Get the nearest unvisited neighbor from a given location.

    Args:
        current_row (float): The list of distances from the current location to all other locations.
        visited_location_indices ([int]): A list of indices representing the visited locations.

    Returns:
        int: The index of the nearest unvisited neighbor.

    Notes:
        time complexity: O(n)
        space complexity: O(1)
    """
    for i in neighbors_sorted_by_distance_from_current_location(current_row): # O(n) - for loop
        if i not in visited_location_indices: # O(n) - in operator
            return i
    return None
