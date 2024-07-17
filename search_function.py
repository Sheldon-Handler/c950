#  MIT License
#
#  Copyright (c) 2024 Sheldon Handler
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice (including the next paragraph) shall be included in all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
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
import hash_table


def specific_package_at_time(
    packages_table: hash_table.HashTable, package_id: int, time: datetime.time = None
) -> package.Package or None:
    found_package = packages_table.get(package_id)

    if found_package is None:
        return None

    new_delivery_status = found_package.delivery_status

    current_address_id, current_address_name, current_address = (
        found_package.address_id,
        found_package.address_name,
        found_package.address,
    )

    if time.__class__ == datetime.time:
        if time < found_package.modified_time:
            current_address_id, current_address_name, current_address = (
                found_package.old_address_id,
                found_package.old_address_name,
                found_package.old_address,
            )
        else:
            current_address_id, current_address_name, current_address = (
                found_package.address_id,
                found_package.address_name,
                found_package.address,
            )

        if time < found_package.arrival_time:
            new_delivery_status = "Not Available"
        elif time < found_package.load_time:
            new_delivery_status = "At Hub"
        elif time < found_package.departure_time:
            new_delivery_status = "At Hub"
        elif time < found_package.delivery_time:
            new_delivery_status = "En Route"
        else:
            new_delivery_status = "Delivered"

    cloned_package = package.Package(
        copy.deepcopy(found_package.id),
        copy.deepcopy(current_address_id),
        copy.deepcopy(current_address_name),
        copy.deepcopy(current_address),
        copy.deepcopy(found_package.city),
        copy.deepcopy(found_package.state),
        copy.deepcopy(found_package.zip),
        copy.deepcopy(found_package.delivery_deadline),
        copy.deepcopy(found_package.weight_kilo),
        copy.deepcopy(found_package.special_notes),
        new_delivery_status,
        copy.deepcopy(found_package.truck_id),
        copy.deepcopy(found_package.arrival_time),
        copy.deepcopy(found_package.load_time),
        copy.deepcopy(found_package.departure_time),
        copy.deepcopy(found_package.delivery_time),
        copy.deepcopy(found_package.modified_time),
    )

    return cloned_package


# def package_status_at_time(
#     packages_list: [package.Package],
#     time: datetime.time = None,
# ) -> [package.Package]:
#     """
#     Returns a list of packages and their statuses at a given time.
#
#     Args:
#         packages_list (list): A list of packages.
#         time (datetime.time): The time to check the statuses of the packages.
#
#     Returns:
#         list: A list of packages and their statuses.
#
#     Notes:
#         time complexity:
#             best case: O(n)
#             worst case: O(n)
#             average case: O(n)
#         space complexity:
#             best case: O(n)
#             worst case: O(n)
#             average case: O(n)
#     """
#     #   cloned_packages_list = copy.deepcopy(packages_list)  # O(n) - deep copy
#     cloned_packages_list = copy.deepcopy(packages_list)  # O(n) - deep copy
#
#     # Check if the time is a datetime.time object
#     if time.__class__ == datetime.time:
#         # Set the status of each package based on the time
#         for package in cloned_packages_list:  # O(n) - for loop
#             if time < package.arrival_time:
#                 package.delivery_status = "Not Available"
#             elif time < package.load_time:
#                 package.delivery_status = "At Hub"
#             elif time < package.departure_time:
#                 package.delivery_status = "At Hub"
#             elif time < package.delivery_time:
#                 package.delivery_status = "En Route"
#             else:
#                 package.delivery_status = "Delivered"
#
#     return cloned_packages_list


def package_status_at_time(
    packages_list: [package.Package],
    time: datetime.time = None,
) -> [package.Package]:
    cloned_packages_list = []

    for i in packages_list:  # O(n) - for loop
        if time.__class__ == datetime.time:
            if time < i.arrival_time:
                i.delivery_status = "Not Available"
            elif time < i.load_time:
                i.delivery_status = "At Hub"
            elif time < i.departure_time:
                i.delivery_status = "At Hub"
            elif time < i.delivery_time:
                i.delivery_status = "En Route"
            else:
                i.delivery_status = "Delivered"

        current_address_id, current_address_name, current_address = (
            i.address_id,
            i.address_name,
            i.address,
        )

        if i.modified_time is not None and i.modified_time > time:
            current_address_id, current_address_name, current_address = (
                i.old_address_id,
                i.old_address_name,
                i.old_address,
            )

        package_copy = package.Package(
            i.id,
            current_address_id,
            current_address_name,
            current_address,
            i.city,
            i.state,
            i.zip,
            i.delivery_deadline,
            i.weight_kilo,
            i.special_notes,
            i.delivery_status,
            i.truck_id,
            i.arrival_time,
            i.load_time,
            i.departure_time,
            i.delivery_time,
            i.modified_time,
        )
        cloned_packages_list.append(package_copy)

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
        distance_visited += __init__.distances[current_address][address_id]
        current_address = address_id

    # Add the distance back to the hub if the truck has returned
    if truck.return_time <= time:
        distance_visited += __init__.distances[current_address][0]

    return distance_visited


def total_distance_traveled(
    trucks: [truck.Truck],
    packages_at_time: [package.Package],
    time: datetime.time,
) -> float:
    """
    Returns the total distance traveled by all trucks at a given time.

    Args:
        trucks (list): A list of trucks.
        packages_at_time (list) : A list of packages at a given time.

    Returns:
        float: total distance traveled by all trucks.

    Notes:
        time complexity:
            best case: O(n^3)
            worst case: O(n^3)
            average case: O(n^3)

        space complexity:
            best case: O(n)
            worst case: O(n)
            average case: O(n)
    """
    total_distance = float(0)

    # Add the distance traveled by each truck to the total distance
    for truck in trucks:  # O(n) - for loop
        total_distance += distance_traveled(truck, packages_at_time, time)

    return total_distance


def distance_traveled_at_time(
    package_list_at_time: [package.Package],
    input_time: datetime.time,
    trucks=__init__.trucks,
):
    distance_traveled_list = []
    truck_view_list = []
    total_distance_traveled_at_time = float(0)
    total_distance_traveled_by_end_of_day = float(0)

    for i in trucks:  # O(n) - for loop
        truck_distance_traveled = distance_traveled(
            i, package_list_at_time, input_time
        )  # O(n^2) - function call

        distance_traveled_list.append(truck_distance_traveled)

        total_distance_traveled_at_time += distance_traveled
        total_distance_traveled_by_end_of_day += i.distance_traveled

        truck_status = ""
        if input_time < i.departure_time:
            truck_status = "At Hub"
        elif i.return_time > input_time:
            truck_status = "En Route"
        elif i.return_time <= input_time:
            truck_status = "At Hub"

        truck_view = truck.TruckView(
            i.id, truck_distance_traveled, i.distance_traveled, truck_status
        )
        truck_view_list.append(truck_view)

    return truck_view_list, total_distance_traveled_at_time
