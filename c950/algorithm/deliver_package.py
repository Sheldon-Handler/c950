from datetime import datetime
from c950.model.package import Package
from c950.model.truck import Truck
from c950.defaults import trucks


def deliver(package: Package, truck: Truck, time: datetime.time) -> bool:
    """
    Delivers a package from a truck at a specific time.

    Args:
        package (Package): The package to deliver.
        truck (Truck): The truck to deliver the package from.
        time (datetime.time): The time of delivery.

    Returns:
        bool: True if the package was delivered successfully, False otherwise.

    Warnings:
        This is a horrible practice. It mutates the truck object and the package object, which are variables located in
        a different module. It is fine for this small and simple project, but it is a bad practice in most cases.

    Notes:
        linear search (for loop):
            time complexity:
                best case = O(1)
                worst case = O(n)
                average case = O(n)
        constant search (if statement):
            time complexity:
                best case = O(1)
                worst case = O(1)
                average case = O(1)
    """
