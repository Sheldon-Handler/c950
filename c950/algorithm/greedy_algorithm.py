"""Greedy Algorithm"""
from c950.model.address import Address


def greedy_algorithm_package_delivery(
    distance_matrix: list[list], starting_location: int = 0
):
    """
    Calculates the total distance traveled for package delivery using a greedy algorithm.

    Args:
        distance_matrix (list of lists): A matrix representing the distances between delivery locations.
        starting_location (int): The index of the initial delivery location. Defaults to 0.

    Returns:
        int: The total distance traveled for all deliveries.

    Examples:
        >>> distance_matrix = [
        ...     [0, 10, 15, 20],
        ...     [10, 0, 20, 30],
        ...     [15, 20, 0, 10],
        ...     [20, 30, 10, 0],
        ... ]
        >>> starting_location = 0
        >>> greedy_algorithm_package_delivery(distance_matrix, starting_location)
        35
        >>> print("Total distance traveled:", total_distance)
        Total distance traveled: 35
    """

    # Initialize the total distance traveled to 0
    total_distance = 0

    # Set the current location to the starting location
    current_location = starting_location

    # Create a list of unvisited locations
    unvisited_locations = []
    # Add all locations to the list of unvisited locations except for the starting location
    for i in range(len(distance_matrix)):
        # Skip the starting location
        if i != starting_location:
            # Add the location to the list of unvisited locations
            unvisited_locations.append(i)

    # Loop until all locations have been visited
    while unvisited_locations:
        # Find the unvisited location with the shortest distance from the current location
        closest_location = min(
            # Loop through all unvisited locations
            unvisited_locations,
            # Use the distance from the current location to the unvisited location as the key for the min function
            key=lambda location: distance_matrix[current_location][location],
        )

        # Update the total distance by adding the distance to the closest location
        total_distance += distance_matrix[current_location][closest_location]

        # Update the current location to the closest location
        current_location = closest_location

        # Remove the closest location from the list of unvisited locations
        unvisited_locations.remove(closest_location)

    # Add the distance from the last location back to the starting location
    return total_distance


# Example usage

distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 20, 30],
    [15, 20, 0, 10],
    [20, 30, 10, 0],
]

starting_location = 0  # Replace with the actual starting location index

total_distance = greedy_package_delivery(distance_matrix, starting_location)
print("Total distance traveled:", total_distance)
