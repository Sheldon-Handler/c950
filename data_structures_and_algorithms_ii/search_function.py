#  MIT License
#
#  Copyright (c) 2024 Sheldon Handler
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice (including the next paragraph) shall be included in all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
import copy
import datetime

import data_structures_and_algorithms_ii
import data_structures_and_algorithms_ii.hash_table
import data_structures_and_algorithms_ii.nearest_neighbor
import data_structures_and_algorithms_ii.package
import data_structures_and_algorithms_ii.truck


def package_lookup(
    package_id: int,
    packages: list
    or data_structures_and_algorithms_ii.hash_table.HashTable = data_structures_and_algorithms_ii.packages,
) -> data_structures_and_algorithms_ii.package.Package or None:
    """
    Looks up a package by its ID.

    Args:
        package_id (int): The ID of the package to search for
        packages (list or data_structures_and_algorithms_ii.hash_table.HashTable): A list of packages. Defaults to the global packages list.

    Returns:
        dict: The package with the specified ID.
    """

    # Check if the packages are stored in a hash table or a list
    if packages.__class__ == data_structures_and_algorithms_ii.hash_table.HashTable:
        return packages.get(package_id)
    elif packages.__class__ == list:
        for package in packages:
            if package.id == package_id:
                return package
    else:
        return None


def package_status_at_time(
    packages_list: [data_structures_and_algorithms_ii.package.Package],
    trucks_list: [data_structures_and_algorithms_ii.truck.Truck],
    time: datetime.time = None,
) -> ([data_structures_and_algorithms_ii.package.Package],):
    """
    Returns a list of packages and their statuses at a given time.

    Args:
        packages_list (list): A list of packages.
        time (datetime.time): The time to check the statuses of the packages.

    Returns:
        list: A list of packages and their statuses.
    """
    cloned_packages_list = [copy.deepcopy(package) for package in packages_list]
    #    cloned_truck_list = [copy.deepcopy(truck) for truck in trucks_list]

    # Check if the time is a datetime.time object
    if time.__class__ == datetime.time:

        # # Set the status of each truck based on the time
        # for truck in cloned_truck_list:  # O(n) - for loop
        #     if time < truck.departure_time:
        #         truck.status = "At Hub"
        #     elif time >= truck.departure_time and time < truck.return_time:
        #         truck.status = "En Route"
        #     else:
        #         truck.status = "At Hub"

        # Set the status of each package based on the time
        for package in cloned_packages_list:  # O(n) - for loop
            if time < package.arrival_time:
                package.delivery_status = "Not Available"
            elif time < package.load_time:
                package.delivery_status = "At Hub"
            elif time < package.departure_time:
                package.delivery_status = "At Hub"
            elif time < package.delivery_time:
                package.delivery_status = "En Route"
            else:
                package.delivery_status = "Delivered"

    return cloned_packages_list


def distance_traveled_and_packages_status(
    truck: data_structures_and_algorithms_ii.truck.Truck,
    packages_at_time: [data_structures_and_algorithms_ii.package.Package],
):
    """
    Returns the distance traveled by each truck at a given time.

    Args:
        truck (data_structures_and_algorithms_ii.truck.Truck): The truck to check the distance of.
        packages_at_time (list) : A list of packages at a given time.

    Returns:
        list: A list of trucks and the distance they have traveled.
    """

    packages_in_truck = []

    for package in packages_at_time:  # O(n) - for loop
        if package.truck_id == truck.id:
            packages_in_truck.append(package)

    # Sort the packages by delivery time
    sorted_packages = sorted(packages_in_truck, key=lambda x: x.delivery_time)

    # Get all the packages that have been delivered
    sorted_packages_delivered = [
        package for package in sorted_packages if package.delivery_status == "Delivered"
    ]  # O(n) - for loop

    # Add all the addresses to a list
    addresses = [0]
    for package in sorted_packages_delivered:  # O(n) - for loop
        if package.address_id not in addresses:  # O(n) - list search
            addresses.append(package.address_id)

    # Calculate the distance traveled
    current_address = addresses[0]
    distance_traveled = 0
    for address in addresses:  # O(n) - for loop
        distance_traveled += data_structures_and_algorithms_ii.distances[
            current_address
        ][address]
        current_address = address

    return distance_traveled
