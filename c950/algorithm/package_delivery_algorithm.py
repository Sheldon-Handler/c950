class PackageGroup:
    """
    Represents a group of packages to be delivered together in a multi-truck delivery scenario.

    Attributes:
        package_locations (list): A list of package locations belonging to the group.
        distance_matrix (list of lists): A matrix representing the distances between delivery locations.
        starting_location (int): The index of the initial delivery location.

    Methods:
        calculate_route(distance_matrix, starting_location): Calculates the route for delivering the packages in the group.
        calculate_distance(distance_matrix, starting_location): Calculates the total distance traveled for delivering the packages in the group.
    """

    def __init__(self, package_locations, distance_matrix, starting_location=0):
        self.package_locations = package_locations
        self.distance_matrix = distance_matrix
        self.starting_location = starting_location

    def calculate_route(self):
        """
        Calculates the optimal route for delivering the packages in the group, considering the starting location.

        Returns:
            list: A list representing the route, with each element representing a package location index.
        """

        route = []
        current_location = self.starting_location

        for location in self.package_locations:
            route.append(location)
            current_location = location

        # Add a return trip to the starting location
        route.append(self.starting_location)

        return route

    def calculate_distance(self) -> float:
        """
        Calculates the total distance traveled for delivering the packages in the group, considering the starting location.

        Returns:
            float: The total distance traveled for delivering all packages in the group.
        """

        total_distance = 0
        current_location = self.starting_location

        for location in self.package_locations:
            total_distance += self.distance_matrix[current_location][location]
            current_location = location

        # Add the distance for the return trip to the starting location
        total_distance += self.distance_matrix[current_location][self.starting_location]

        return total_distance


def multi_truck_greedy_package_delivery_with_grouping(
    distance_matrix, starting_location, truck_capacity, truck_speed, num_trucks
):
    """
    Calculates the total distance traveled for package delivery using a greedy algorithm with package grouping, considering truck speed and number of trucks.

    Args:
        distance_matrix (list of lists): A matrix representing the distances between delivery locations.
        starting_location (int): The index of the initial delivery location.
        truck_capacity (int): The maximum number of packages that a truck can carry.
        truck_speed (float): The speed of the truck in miles per hour.
        num_trucks (int): The number of trucks available for delivery.

    Returns:
        tuple: A tuple containing the total distance traveled, a list of truck routes (represented as dictionaries), and a list of estimated delivery times.
    """

    total_distance = 0
    trucks = []
    estimated_delivery_times = []

    # Calculate package loading groups
    package_groups = calculate_package_loading_groups(
        distance_matrix, starting_location, truck_capacity
    )

    # Assign package groups to trucks
    for package_group in package_groups:
        # Check if there are available trucks
        if len(trucks) < num_trucks:
            # Create a PackageGroup instance and calculate its route and distance
            package_group_instance = PackageGroup(package_group)
            route = package_group_instance.calculate_route(
                distance_matrix, starting_location
            )
            distance = package_group_instance.calculate_distance(
                distance_matrix, starting_location
            )

            # Calculate estimated delivery time based on truck speed and distance
            estimated_delivery_time = distance / truck_speed

            # Add the truck and estimated delivery time to the corresponding lists
            trucks.append({"route": route, "distance": distance})
            estimated_delivery_times.append(estimated_delivery_time)

    # Update the total distance traveled by all trucks
    for truck in trucks:
        total_distance += truck["distance"]

    return total_distance, trucks, estimated_delivery_times
