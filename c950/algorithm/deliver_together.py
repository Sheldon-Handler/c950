from c950.model.package import Package
from c950 import packages

delivery_groups = list([])


def add(package):
    for package.special_notes_attribute_value in packages:
        if package.special_notes_attribute_value == package.id:
            delivery_groups.append(package.id)
            return


def add_to_delivery_group(package: Package) -> bool:
    """
    Adds a package to a delivery group.

    Args:
        package_id (int): The id of the package to add to a delivery group.

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


def search_delivery_groups_for_package_id(package_id: int) -> int or None:
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
