import datetime

import data_structures_and_algorithms_ii
import data_structures_and_algorithms_ii.address


class Truck:
    """This class represents a truck instance with its information.

    Attributes:
        id (int): The ID of the truck.
        truck_status (TruckStatus): The status of the truck.
        distance_traveled (float): The distance the truck has traveled.
        packages (list[int]): The list of package IDs the truck is carrying.


    Returns:
        Truck: A Truck class instance.
    """

    def __init__(
        self,
        id: int,
        truck_status: str,
        distance_traveled: float = None,
        packages: [int] = None,
        capacity: int = data_structures_and_algorithms_ii.truck_capacity,
    ):
        """
        Initializes the truck class with its information.

        Args:
            id: The ID of the truck.
            truck_status: The status of the truck.
            distance_traveled: The distance the truck has traveled.
            packages: The list of package IDs the truck is carrying.
        """
        self.id = id
        self.truck_status = truck_status
        self.distance_traveled = distance_traveled
        self.packages = packages
        self.truck_time = datetime.timedelta(hours=8, minutes=0)

    def update_truck_status(self, truck_status: str) -> bool:
        """Updates the truck status.

        Args:
            truck_status (TruckStatus): The status of the truck.

        Returns:
            bool: True if the truck_status is valid and updated accordingly. Otherwise, raises a ValueError.
        """

        truck_statuses = ["Not Available", "At Hub", "En Route", "Returning"]

        if truck_status in truck_statuses:
            self.truck_status = truck_status
            print(f"Truck {self.id} status updated to {self.truck_status}.")
            return True
        else:
            raise ValueError(
                f"Truck status must be one of the following: {truck_statuses}."
            )

    def load_packages_with_address(
        self, address: data_structures_and_algorithms_ii.address.Address
    ) -> bool:
        """Loads a package onto the truck.

        Args:
            address (data_structures_and_algorithms_ii.address.Address): The ID of the package to load onto the truck.

        Returns:
            bool: True if a package was loaded successfully. Otherwise, raises a ValueError.
        """

        package_loaded = False

        for package in data_structures_and_algorithms_ii.packages:  # O(n) - for loop
            if package.address == address:
                self.packages.append(package.id)
                package.truck_id = self.id
                package.delivery_status = "En Route"
                print(f"Package {package.id} loaded onto truck {self.id}.")
                address.addresses.get(package.address)
                package_loaded = True

        return package_loaded
