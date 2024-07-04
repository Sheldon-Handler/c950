#  MIT License
#
#  Copyright (c) 2024 Sheldon Handler
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice (including the next paragraph) shall be included in all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
import datetime

import data_structures_and_algorithms_ii
import data_structures_and_algorithms_ii.hash_table
import data_structures_and_algorithms_ii.package


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
    time: datetime.time = None,
) -> [data_structures_and_algorithms_ii.package.Package]:
    """
    Returns a list of packages and their statuses at a given time.

    Args:
        packages_list (list): A list of packages.
        time (datetime.time): The time to check the statuses of the packages.

    Returns:
        list: A list of packages and their statuses.
    """

    # Check if the time is None
    if time is None:
        # Set the status all to the end of day values
        for package in packages_list:  # O(n) - for loop
            package.delivery_status = "Delivered"

    # Check if the time is a datetime.time object
    elif time.__class__ == datetime.time:
        # Set the status of each package based on the time
        for package in packages_list:  # O(n) - for loop
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

    # If the time is not a datetime.time object, raise an exception
    else:
        raise Exception("Invalid time")

    return packages_list
