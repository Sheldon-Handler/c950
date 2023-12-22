import datetime

import c950
from c950 import truck_capacity, starting_location, distances, packages
from c950.model.package import Package
from c950.model.truck import Truck


def load_truck(
    truck: Truck,
    packages: list[Package],
    load_time: datetime.time = datetime.datetime.now().time(),
    distances: list[list[float]] = distances,
    starting_location: int = starting_location,
    truck_capacity: int = truck_capacity,
):
    """
    Loads packages onto trucks for delivery.

    Returns:
        list: A list of Truck objects, each containing a list of packages to be delivered.

    Notes:
        time complexity: O(n^2)
        space complexity: O(1)
    """

    __packages_that_can_only_be_on_truck__(truck, packages)

    for package in packages:
        if (
            package.special_notes_attribute_key == "Can only be on truck"
            and package.special_notes_attribute_value != truck.id
            and check_if_package_can_be_loaded(package, truck) is True
        ):
            package.truck_id = truck.id
            package.delivery_time = load_time
            package.delivery_status = "En Route"
            truck.packages.append(package.id)


def check_if_package_can_be_loaded(
    package: Package,
    truck: Truck,
    load_time: datetime.time = datetime.datetime.now().time(),
    current_time: datetime.time = datetime.datetime.now().time(),
) -> bool:
    """
    Checks if the given package can be loaded onto the given truck.

    Args:
        package (Package): The package to load.
        truck (Truck): The truck to load the package onto.
        load_time (datetime.time): The time to load the package. Defaults to current time.

    Returns:
        list: A list of Truck objects, each containing a list of packages to be delivered.

    Notes:
        time complexity: O(1)
        space complexity: O(1)
    """

    if (
        package.special_notes_attribute_key == "Can only be on truck"
        and package.special_notes_attribute_value != truck.id
    ):
        print(
            f"Package {package.id} cannot be loaded onto Truck {truck.id} at {package.delivery_time}."
            f" It can only be loaded onto Truck {package.special_notes_attribute_value}."
        )
        return False
    elif (
        package.special_notes_attribute_key
        == "Delayed on flight---will not arrive to depot until"
        and current_time < package.special_notes_attribute_value
    ):
        print(
            f"Package {package.id} cannot be loaded onto Truck {truck.id} at {package.delivery_time}."
            f" It will not arrive to the depot until {package.special_notes_attribute_value}."
        )
        return False
    elif package.special_notes_attribute_key == "Wrong address listed":
        print(
            f"Package {package.id} cannot be loaded onto Truck {truck.id} because the wrong address is assigned."
        )
        return False
    elif package.delivery_status == "Not Available":
        print(
            f"Package {package.id} is Not Available. Cannot load onto truck {truck.id}"
        )
        return False
    elif package.delivery_status == "En Route":
        print(
            f"Package {package.id} is currently En Route on Truck {package.truck_id}."
        )
        return False
    elif package.delivery_status == "Delivered":
        print(
            f"Package {package.id} has already been delivered from Truck {package.truck_id} at {package.delivery_time}."
        )
        return False
    elif package.delivery_status == "At Hub" and package.truck_id != (truck.id or None):
        print(f"Package {package.id} is already loaded onto Truck {package.truck_id}.")
        return False
    elif len(truck.packages) >= c950.truck_capacity:
        print(
            f"Truck {truck.id} is currently full. Cannot load package {package.id} onto it."
        )
        return False
    elif truck.truck_status == "Not Available" and truck.id != package.truck_id:
        print(
            f"Truck {truck.id} is Not Available. Cannot load package {package.id} onto it."
        )
        return False
    elif truck.truck_status == "En Route" and truck.id != package.truck_id:
        print(f"Truck {truck.id} En Route. Cannot load package {package.id} onto it.")
        return False
    elif truck.truck_status == "Returning" and truck.id != package.truck_id:
        print(
            f"Truck {truck.id} is not available. Cannot load package {package.id} onto it."
        )
        return False
    else:
        return True


def __packages_that_can_only_be_on_truck__(
    truck: Truck, packages: list[Package] = packages
) -> list[Package]:
    """
    Returns a list of packages that can only be on a specific truck.

    Args:
        truck: (Truck): The truck to check.
        packages (list[Package]): A list of packages.

    Returns:
        list: A list of packages that can only be on a specific truck.

    Notes:
        time complexity: O(n)
        space complexity: O(1)
    """

    packages_that_can_only_be_on_truck = []

    # Find the packages that can only be on a specific truck and add them to the list
    for package in packages:  # O(n) - for loop
        if (
            package.special_notes_attribute_key == "Can only be on truck"
            and package.special_notes_attribute_value == truck.id
        ):
            packages_that_can_only_be_on_truck.append(package)

    return packages_that_can_only_be_on_truck


def __load_truck_without_checking__(truck: Truck, package: Package) -> None:
    """
    Loads packages onto trucks for delivery.

    Returns:
        truck: (Truck): The truck to load the package onto.
        package: (Package): The package to load onto the truck.

    Notes:
        time complexity: O(1)
        space complexity: O(1)
    """

    package.truck_id = truck.id
    package.delivery_status = "En Route"
    truck.packages.append(package.id)
