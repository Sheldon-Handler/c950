def sorted_neighbors(distances_list: [float]) -> [int]:
    """
    Sorts a list and returns a list of indexes sorted by the corresponding value in ascending order.

    Args:
        distances_list: The list to be sorted.

    Returns:
        A list of indexes whose values are sorted from small to high.

    Notes:
        time complexity: O(n^2 log n)
        space complexity: O(n)
    """

    items_sorted = [
        i[0] for i in sorted(enumerate(distances_list), key=lambda x: x[1])
    ]  # O(n^2 log n)

    return items_sorted


def sorted_unvisited_neighbors(
    distances_list: [float], visited_location_indices: [int]
) -> [int] or None:
    """
    Get the nearest unvisited neighbor from a given location.

    Args:
        distances_list ([float]): The list of distances from the current location to all other locations.
        visited_location_indices ([int]): A list of indices representing the visited locations.

    Returns:
        [int] or None: The index of the nearest unvisited neighbor. None if all locations have been visited.

    Notes:
        time complexity: O(n^2 log n)
        space complexity: O(n)
    """
    unvisited_location_indices = []
    sorted_neighbors_list = sorted_neighbors(
        distances_list
    )  # O(n^2 log n) - function call

    for i in sorted_neighbors_list:  # O(n) - for loop
        if i not in visited_location_indices:  # O(n) - list search
            unvisited_location_indices.append(i)

    return unvisited_location_indices
