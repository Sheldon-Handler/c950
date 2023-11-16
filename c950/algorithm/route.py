def route_packages(distance_matrix):
    """
    Routes package deliveries using a distance matrix.

    Args:
        distance_matrix (list[list]): A two-dimensional list where each element represents
            the distance between two locations.

    Returns:
        list[list]: A list of delivery routes, where each route is a list of the indices
            of the packages to be delivered on that route.

    """

    # Create a list to store the delivery routes
    delivery_routes = []

    # Create a list to track which packages have not been delivered
    undelivered_packages = list(range(len(distance_matrix)))

    # While there are still undelivered packages
    while undelivered_packages:
        # Find the closest undelivered package to the current delivery location
        closest_package_index = None
        min_distance = float("inf")
        for i in undelivered_packages:
            dist = distance_matrix[current_delivery_location][i]
            if dist < min_distance:
                closest_package_index = i
                min_distance = dist

        # Add the closest undelivered package to the current delivery route
        current_delivery_route.append(closest_package_index)

        # Mark the package as delivered
        undelivered_packages.remove(closest_package_index)

        # If the current delivery route is full, add it to the list of delivery routes
        if len(current_delivery_route) == capacity:
            delivery_routes.append(current_delivery_route)
            current_delivery_location = 0
            current_delivery_route = []

        # Otherwise, set the current delivery location to the last package delivered
        else:
            current_delivery_location = closest_package_index

    # If there are any remaining undelivered packages, add them to a new delivery route
    if undelivered_packages:
        current_delivery_route = undelivered_packages
        delivery_routes.append(current_delivery_route)

    return delivery_routes
