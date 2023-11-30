from c950.model.package import *
from c950.model.truck import *
from c950.model.truck import Truck
from c950.defaults import *


def load_package(
    package_id: int = None,
    truck_id: int = None,
    packages: list[Package] = packages,
    trucks: list[Truck] = trucks,
) -> bool:
    """
    Loads a package onto a truck.

    Args:
        package_id (Package): The id of the package to load onto the truck.
        truck_id (int): The id of the truck to load the package onto.
        packages (list): A list of Package objects.
        trucks (list): A list of Truck objects.

    Returns:
        bool: True if the package was loaded onto the truck. Otherwise, False.

    Notes:
        time complexity: O(n^2)
        space complexity: O(1)
    """

    # Ensure that package_id and truck_id are provided
    if package_id is None or truck_id is None:
        print("package_id and truck_id must be provided.")
        return False

    package_index = get_index_of_package_by_id(package_id, packages)  # O(n)
    truck_index = get_index_of_truck_by_id(truck_id, trucks)  # O(n)

    if package_index is None:
        print(f"Package with id {package_id} not found.")
        return False
    elif truck_index is None:
        print(f"Truck with id {truck_id} not found.")
        return False
    else:
        packages[package_index].load_onto_truck(truck_id)
        trucks[truck_index].load_package(packages[package_index])
