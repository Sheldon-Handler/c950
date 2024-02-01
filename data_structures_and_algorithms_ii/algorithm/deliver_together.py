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


delivery_groups = list([])


def get_delivery_groups() -> list:
    """
    Returns the delivery groups.

    Returns:
        list: The delivery groups.

    Notes:
        time complexity: O(1)
        space complexity: O(1)
    """

    return delivery_groups


def set_delivery_groups() -> None:
    """
    Sets the delivery groups for packages that must be delivered together.

    Returns:
        None

    Notes:
        time complexity: O(n)
        space complexity: O(1)
    """

    # Find the packages that must be delivered together and add them to the list
    for package in data_structures_and_algorithms_ii.packages:  # O(n) - for loop
        if package.special_notes_attribute_key == "Must be delivered with":
            add_to_delivery_group(package)


def add_to_delivery_group(
    package,
) -> bool:
    """
    Adds a package to a delivery group.

    Args:
        package (Package): The package to add to a delivery group.

    Returns:
        bool: True if the package was added to a delivery group, False if not.

    Notes:
        time complexity: O(n^3)
        space complexity: O(1)
    """

    # Find the delivery group that the package belongs to and add it to the list
    for delivery_group in delivery_groups:  # O(n) - for loop
        # Find the packages that must be delivered together and add them to the list
        for (
            other_package_id
        ) in package.special_notes_attribute_value:  # O(n) - for loop
            # If the package belongs to a delivery group, add it to the delivery group
            for _ in delivery_group:  # O(n) - for loop
                if other_package_id in delivery_group:
                    delivery_group.append(package.id)
                    print(
                        "Package with id={} added to delivery group index {}.".format(
                            package.id, delivery_group
                        )
                    )
                    return True
                elif package.id in delivery_group:
                    print(
                        "Package with id={} already in delivery group {}.".format(
                            package.id, delivery_group
                        )
                    )
                    return False

    # If the package does not belong to a delivery group, create a new delivery group
    new_delivery_group = []
    # Add the package to the new delivery group
    new_delivery_group.append(package.id)
    # Add the new delivery group to the list of delivery groups
    delivery_groups.append(new_delivery_group)
    print(
        "New delivery group created at index {}. Package with id={} added to it.".format(
            len(delivery_groups) - 1, package.id
        )
    )
    return True


def search_delivery_groups_for_package_id(package_id) -> int or None:
    """
    Searches for a package id that must be delivered together.

    Returns:
        int: The index of the delivery group that the package belongs to.

    Notes:
        time complexity: O(n^3)
        space complexity: O(1)
    """

    for delivery_group in delivery_groups:  # O(n) - for loop
        if package_id in delivery_group:  # O(n) - in operator
            return delivery_groups.index(delivery_group)  # O(n) - index method

    return None
