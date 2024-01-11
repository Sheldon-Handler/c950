#  MIT License
#
#  Copyright (c) 2023 Sheldon Handler
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice (including the next paragraph) shall be included in all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#


def greedy_truck_assignment(distance_matrix, packages_per_truck=40, num_trucks=2):
    """
    Assigns packages to trucks using a greedy algorithm.

    Args:
        distance_matrix (list[list[float]]): A matrix of distances between locations.
        packages_per_truck (int): The number of packages that each truck can carry.
        num_trucks (int): The number of trucks available for delivery.

    Returns:
        list[list[int]]: A list of lists, where each inner list represents the route of a single truck.
    """

    unassigned_packages = set(
        range(1, len(distance_matrix))
    )  # Packages are indexed from 1
    assigned_packages = []  # Packages that have been assigned to a the truck
    truck_routes = [
        [] for _ in range(num_trucks)
    ]  # A list of lists. Each inner list represents route of single truck.

    while unassigned_packages:  # Assign packages to trucks using the greedy algorithm
        # Find the truck with the shortest distance to an unassigned package
        shortest_distance = float("inf")
        closest_truck = None
        closest_package = None

        # Find the closest truck and package
        for truck_index, truck_route in enumerate(truck_routes):
            for package_index in unassigned_packages:
                distance = distance_matrix[truck_route[-1]][package_index]
                if distance < shortest_distance:
                    shortest_distance = distance
                    closest_truck = truck_index
                    closest_package = package_index

        # Assign the closest package to the closest truck
        truck_routes[closest_truck].append(closest_package)
        unassigned_packages.remove(closest_package)

        # Check if the truck's capacity is reached
        if len(truck_routes[closest_truck]) == packages_per_truck:
            # Return to the starting location to reload the truck
            truck_routes[closest_truck].append(0)

    return truck_routes
