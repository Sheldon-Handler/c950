from c950.model.package import Package
from c950.model.truck import Truck
from c950.defaults import (
    distances,
    truck_capacity,
    visited_location_indices,
    starting_location,
)


def load_truck(
    truck_id: int,
    packages: list[Package],
    distances: list[list[float]] = distances,
    starting_location: int = starting_location,
    truck_capacity: int = 16,
):
    """
    Loads packages onto trucks for delivery.

    Returns:
        list: A list of Truck objects, each containing a list of packages to be delivered.
    """

    __packages_that_can_only_be_on_truck__(truck_id, packages)


    for package in packages:
        if package.special_notes_attribute_key == "Can only be on truck" \
            and package.special_notes_attribute_value != truck_id:


    for package in packages:
        if (
            check_if_package_can_be_loaded(package, truck_id) is True
        ):
            package.delivery_status = "En Route"
            package.truck_id = truck_id
            package.delivery_time = "8:00 AM"
            visited_location_indices.append(package.id)
            print(
                f"Package {package.id} loaded onto Truck {truck_id} at {package.delivery_time}."
            )


def check_if_package_can_be_loaded(
    package: Package,
    truck_id: int,
    distances: list[list[float]] = distances,
    starting_location: int = starting_location,
    truck_capacity: int = truck_capacity,
) -> bool:
    """
    Checks if a package can be loaded onto a truck.

    Args:
        package (Package): A package.
        truck_id (int): The id of the truck.
        distances (list[list[float]]): A list of lists representing the distance matrix.
        starting_location (int): The index of the starting location. Defaults to 0.
        truck_capacity (int): The capacity of the truck. Defaults to 16.

    Returns:
        list: A list of Truck objects, each containing a list of packages to be delivered.

    Notes:
        time complexity: O(1)
        space complexity: O(1)
    """

    if (
        package.special_notes_attribute_key == "Can only be on truck"
        and package.special_notes_attribute_value != truck_id
    ):
        print(
            f"Package {package.id} cannot be loaded onto Truck {truck_id} at {package.delivery_time}."
            f" It can only be loaded onto Truck {package.special_notes_attribute_value}."
        )
        return False
    elif (
        package.special_notes_attribute_key
        == "Delayed on flight---will not arrive to depot until"
    ):
        print(
            f"Package {package.id} cannot be loaded onto Truck {truck_id} at {package.delivery_time}."
            f" It will not arrive to the depot until {package.special_notes_attribute_value}."
        )
        return False
    elif package.special_notes_attribute_key == "Wrong address listed":
        print(
            f"Package {package.id} cannot be loaded onto Truck {truck_id} because the wrong address is assigned."
        )
        return False
    elif package.delivery_status == "Delivered":
        print(
            f"Package {package.id} has already been delivered from Truck {package.truck_id} at {package.delivery_time}."
        )
        return False
    elif package.delivery_status == "En Route":
        print(
            f"Package {package.id} is currently En Route on Truck {package.truck_id}."
        )
        return False
    elif package.delivery_status == "At Hub" and package.truck_id != (truck_id or None):
        print(f"Package {package.id} is already loaded onto Truck {package.truck_id}.")
        return False
    elif (
        package.delivery_status == "At Hub"
        and package.truck_id == truck_id
        and package.special_notes_attribute_key != "Wrong address listed"
    ):
        print(f"Package {package.id} is already loaded onto Truck {truck_id}.")
        return False
    else:
        return True


def __packages_that_can_only_be_on_truck__(truck_id: int, packages: list[Package]) -> list[int]:
    """
    Returns a list of packages that can only be on a specific truck.

    Args:
        truck_id (int): The id of the truck.
        packages (list[Package]): A list of packages.

    Returns:
        list: A list of packages that can only be on a specific truck.

    Notes:
        time complexity: O(n)
        space complexity: O(1)
    """

    package_ids_that_can_only_be_on_truck = []

    # Find the packages that can only be on a specific truck and add they're id's to the list
    for package in packages:
        if package.special_notes_attribute_key == "Can only be on truck" \
                and package.special_notes_attribute_value == truck_id:
            package_ids_that_can_only_be_on_truck.append(package.id)

    return package_ids_that_can_only_be_on_truck


def __load_package__(package: Package, truck: Truck):
    """
    Loads a package onto a truck. Does not check if the package can be loaded onto the truck.

    Args:
        package (Package): A package.
        trucks (list): A list of Truck objects.

    Returns:
        list: A list of Truck objects, each containing a list of packages to be delivered.

    Notes:
        time complexity: O(1)
        space complexity: O(1)
    """

    if truck.truck_status == "At Hub":
        package.truck_id = truck.id
        package.update_delivery_status("En Route")
