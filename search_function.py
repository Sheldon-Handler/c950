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

import __init__
import package
import truck


def package_status_at_time(
        packages_list: [package.Package],
        time: datetime.time = None,
) -> [package.Package]:
    """
    Returns a list of packages and their statuses at a given time.

    Args:
        packages_list (list): A list of packages.
        time (datetime.time): The time to check the statuses of the packages.

    Returns:
        list: A list of packages and their statuses.

    Notes:
        time complexity:
            best case: O(n)
            worst case: O(n)
            average case: O(n)
        space complexity:
            best case: O(n)
            worst case: O(n)
            average case: O(n)
    """
    cloned_packages_list = copy.deepcopy(packages_list)  # O(n) - deep copy

    # Check if the time is a datetime.time object
    if time.__class__ == datetime.time:

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


def distance_traveled(
        truck: truck.Truck,
        packages_at_time: [package.Package],
        time: datetime.time,
) -> float:
    """
    Returns the distance traveled by each truck at a given time.

    Args:
        truck (data_structures_and_algorithms_ii.truck.Truck): The truck to check the distance of.
        packages_at_time (list) : A list of packages at a given time.

    Returns:
        float: distance traveled by the truck.

    Notes:
        time complexity:
            best case: O(n^2)
            worst case: O(n^2)
            average case: O(n^2)

        space complexity:
            best case: O(n)
            worst case: O(n)
            average case: O(n)
    """

    # Add all the packages in the truck to a list
    packages_in_truck = []
    for package in packages_at_time:  # O(n) - for loop
        if package.truck_id == truck.id:
            packages_in_truck.append(package)

    # Sort the packages by delivery time
    packages_in_truck = sorted(
        packages_in_truck, key=lambda x: x.delivery_time
    )  # O(n log n) - sort

    # Add all the delivered packages to a list
    delivered_packages = []
    for package in packages_in_truck:  # O(n) - for loop
        if package.delivery_status == "Delivered":
            delivered_packages.append(package)

    # Add all the addresses of the delivered packages to a list
    delivered_addresses = [0]
    for package in delivered_packages:  # O(n) - for loop
        address_id = package.address_id
        if address_id not in delivered_addresses:  # O(n) - list search
            delivered_addresses.append(address_id)

    # Calculate the distance traveled by the truck
    current_address = 0
    distance_visited = float(0)

    # Add the distances between the delivered addresses
    for address_id in delivered_addresses:  # O(n) - for loop
        distance_visited += __init__.distances[
            current_address
        ][address_id]
        current_address = address_id

    # Add the distance back to the hub if the truck has returned
    if truck.return_time <= time:
        distance_visited += __init__.distances[
            current_address
        ][0]

    return distance_visited
