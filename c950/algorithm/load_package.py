from c950.model.package import Package
from c950.model.truck import Truck
from c950.defaults import truck_capacity


def _load_package(package: Package, truck: Truck):
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

    if truck.truck_status == "At Hub" and len(truck.packages) < truck_capacity:
        package.truck_id = truck.id
        package.update_delivery_status("En Route")
        truck.packages.append(package.id)
