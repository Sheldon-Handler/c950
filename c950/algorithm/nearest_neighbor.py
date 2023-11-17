import sys


# Nearest Neighbor Algorithm (Greedy Algorithm)
## time complexity: O(n)
## space complexity: O(n)
def nearest_neighbor_index(current_location_index: int, distance_matrix: list[list], visited_location_indices: set) -> int:
    """
    Finds the nearest location to the current location from a list of locations.

    Args:
        current_location_index (int): The index of the current location.
        distance_matrix (list[list]): A list of lists representing the distance matrix.
        visited_location_indices (list[int]): A list of indices representing the visited locations.

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
    location_sublist = distance_matrix[current_location_index] # O(1) - assignment

    # Initialize the nearest location index and distance. Default to the first location in the sublist
    nearest_location_index = 0 # O(1) - assignment
    # Initialize the nearest location distance. Default to the first location in the sublist.
    nearest_location_distance = float('inf') # O(1) - assignment

    for i in location_sublist:
        if i != current_location_index and i != 0:
            if nearest_location_distance > location_sublist[i]:
                nearest_location_distance = location_sublist[i]
                nearest_location_index = i

    # Return the index of the nearest location
    return nearest_location_index


def method_name(current_location_index, location_sublist, nearest_location_distance, nearest_location_index):
    # Search for the nearest location (the location with the shortest distance)
    for i in location_sublist:  # O(n) - for loop
        # Ensure that the current location and the hub location is not included when finding the nearest location.
        if i != current_location_index and i != 0:
            # If nearest_location_distance is greater than the distance to location i in the location_sublist
            if nearest_location_distance > location_sublist[i]:
                # Set nearest_location_distance to the distance to location i in the location_sublist
                nearest_location_distance = location_sublist[i]
                # Set nearest_location_index to the index of location i in the location_sublist
                nearest_location_index = i
    return nearest_location_index

def method_name1(current_location_index, location_sublist, nearest_location_distance, nearest_location_index):

    for i in location_sublist:  # O(n) - for loop
        if __find_closer_location__(current_location_index,
                             currently_selected_next_location_index,
                             new_next_location_index,
                             currently_selected_next_location_distance,
                             new_next_location_distance,
                             visited_location_indices,
                             )
                # Set nearest_location_distance to the distance to location i in the location_sublist
                nearest_location_distance = location_sublist[i]
                # Set nearest_location_index to the index of location i in the location_sublist
                nearest_location_index = i
    return nearest_location_index

def __find_closer_location__(current_location_index,
                             currently_selected_next_location_index,
                             new_next_location_index,
                             currently_selected_next_location_distance,
                             new_next_location_distance,
                             visited_location_indices,
                             ):



    if new_next_location_index == 0 \
        or new_next_location_index == current_location_index \
        or new_next_location_index in visited_location_indices:
        return current_location_index
    elif new_next_location_distance < currently_selected_next_location_distance:
        return new_next_location_index