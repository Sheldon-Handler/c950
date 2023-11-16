class AddressGroup:
    """This class represents a group of addresses to deliver packages to together in a multi-truck delivery scenario."""

    def __init__(self):
        self.addresses_assigned = []
        self.distances_between_addresses_assigned = []
        self.starting_location = 0
        self.current_location = 0
        self.route = []
        self.distance_traveled = 0


def calculate_package_loading_groups(
    distance_matrix, starting_location, truck_capacity
):
    """
    Calculates groups of packages based on proximity to each other for multi-truck package delivery.

    Args:
        distance_matrix (list of lists): A matrix representing the distances between delivery locations.
        starting_location (int): The index of the initial delivery location.
        truck_capacity (int): The maximum number of packages that a truck can carry.

    Returns:
        list of lists: A list of lists, where each inner list represents a group of packages to be delivered together.
    """

    # Sort unvisited locations based on their distance from the starting location
    unvisited_locations = list(range(len(distance_matrix)))
    sorted_locations = sorted(
        unvisited_locations,
        key=lambda location: distance_matrix[starting_location][location],
    )

    # Create groups of packages based on proximity
    package_groups = []
    current_group = []

    for location in sorted_locations:
        # Check if the current group has capacity for more packages
        if len(current_group) < truck_capacity:
            current_group.append(location)
        else:
            # If the current group is full, add it to the list of groups and start a new group
            package_groups.append(current_group.copy())
            current_group.clear()
            current_group.append(location)

    # Add the last group if it's not empty
    if current_group:
        package_groups.append(current_group.copy())

    return package_groups
