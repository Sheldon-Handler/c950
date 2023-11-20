

# Nearest Neighbor Algorithm (Greedy Algorithm)
## time complexity: O(n)
## space complexity: O(1)
def nearest_neighbor_index(current_location_index: int, distance_matrix: list[list], visited_location_indices: set, hub_location_index: int = 0) -> int:
    """
    Finds the nearest location to the current location from a list of locations. The nearest location is the location
    with the shortest distance from the current location.

    Args:
        current_location_index (int): The index of the current location.
        distance_matrix (list[list]): A list of lists representing the distance matrix.
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
    location_sublist = distance_matrix[current_location_index]

    # Initialize the nearest location index and distance. Default to the first location in the sublist
    nearest_location_index = 0
    # Initialize the nearest location distance. Default to the first location in the sublist.
    nearest_location_distance = float('inf')

    # Search for the nearest location (the location with the shortest distance)
    for i in location_sublist:  # O(n) - for loop
        # If the current_location_index, hub_location, visited_location_indices are not included when finding
        # the nearest location; and that the currently assigned nearest_location_distance is greater than the distance
        # to location i in the location_sublist.
        if i != current_location_index \
            and i != hub_location_index \
            and i not in visited_location_indices \
            and nearest_location_distance > location_sublist[i]:
            # Set nearest_location_distance to the distance to location i in the location_sublist
            nearest_location_distance = location_sublist[i]
            # Set nearest_location_index to the index of location i in the location_sublist
            nearest_location_index = i

    # Return the index of the nearest location
    return nearest_location_index
