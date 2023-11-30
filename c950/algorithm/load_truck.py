from c950.model.package import Package
from c950.model.truck import Truck
from c950.defaults import *
from c950.algorithm.load_package import _load_package


def load_truck(
    truck: Truck,
    packages: list[Package],
    distances: list[list[float]] = distances,
    starting_location: int = starting_location,
    truck_capacity: int = 16,
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
        if package.special_notes_attribute_key == "Can only be on truck" \
            and package.special_notes_attribute_value != truck.id \
                and check_if_package_can_be_loaded(package, truck) is True:
            _load_package(package, truck)


def check_if_package_can_be_loaded(
    package: Package,
    truck: Truck,
) -> bool:
    """
    Checks if a package can be loaded onto a truck.

    Args:
        package (Package): A package.
        truck (Truck): The truck.

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
    elif package.delivery_status == "At Hub" and package.truck_id != (truck.id or None):
        print(f"Package {package.id} is already loaded onto Truck {package.truck_id}.")
        return False
    elif (
        package.delivery_status == "At Hub"
        and package.truck_id == truck.id
        and package.special_notes_attribute_key != "Wrong address listed"
    ):
        print(f"Package {package.id} is already loaded onto Truck {truck.id}.")
        return False
    else:
        return True


def trucks_with_exclusive_packages():
    """
    Returns a list of trucks with packages that can only be on a specific truck.

    Args:
        trucks (list[Truck]): A list of Truck objects.
        packages (list[Package]): A list of Package objects.

    Returns:
        list: A list of Truck objects, each containing a list of packages to be delivered.

    Notes:
        time complexity: O(n^2)
        space complexity: O(1)
    """

    for truck in trucks:
        for package in truck.packages:
            if package.special_notes_attribute_key == "Can only be on truck"\
                    and package.special_notes_attribute_value == truck.id:
                _load_package(package, truck)

    return trucks_with_exclusive_packages


def __packages_that_can_only_be_on_truck__(truck: Truck, packages: list[Package]) -> list[int]:
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

    package_ids_that_can_only_be_on_truck = []

    # Find the packages that can only be on a specific truck and add they're id's to the list
    for package in packages:
        if package.special_notes_attribute_key == "Can only be on truck" \
                and package.special_notes_attribute_value == truck.id:
            package_ids_that_can_only_be_on_truck.append(package.id)

    return package_ids_that_can_only_be_on_truck
