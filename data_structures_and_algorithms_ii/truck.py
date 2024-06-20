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
        departure_time: datetime.timedelta = None,
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
        self.departure_time = departure_time
        self.truck_time = self.departure_time

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

    # def load_packages_with_address(
    #     self, address: data_structures_and_algorithms_ii.address.Address
    # ) -> bool:
    #     """Loads a package onto the truck.
    #
    #     Args:
    #         address (data_structures_and_algorithms_ii.address.Address): The ID of the package to load onto the truck.
    #
    #     Returns:
    #         bool: True if a package was loaded successfully. Otherwise, raises a ValueError.
    #     """
    #
    #     package_loaded = False
    #
    #     for package in data_structures_and_algorithms_ii.packages:  # O(n) - for loop
    #         if package.address == address:
    #             self.packages.append(package.id)
    #             package.truck_id = self.id
    #             package.delivery_status = "En Route"
    #             print(f"Package {package.id} loaded onto truck {self.id}.")
    #             data_structures_and_algorithms_ii.addresses.get(package.address)
    #             package_loaded = True
    #
    #     return package_loaded

    def load_truck(self, package_id: int) -> None:
        """Loads a package onto the truck.

        Args:
            package_id (int): The ID of the package to load onto the truck.

        Returns:
            None

        Notes:
            time complexity:
                best case = O(1)
                worst case = O(n)
                average case = O(n)
            space complexity:
                best case = O(1)
                worst case = O(1)
                average case = O(1)
        """
        # Find package in the package hash table
        package = data_structures_and_algorithms_ii.packages.get(
            package_id
        )  # O(n) - hash table get
        # Run the load_package method on the package
        package.load_package(self.id)
        # Update the package in the package hash table
        data_structures_and_algorithms_ii.packages.update(
            package_id, package
        )  # O(n) - hash table update

    def send_truck(self, departure_time: datetime.time):
        """Sends the truck to deliver the packages. Updates departure_time and delivery_status attributes of the
        packages in the truck.

        Args:
            departure_time (datetime.time): The time that the truck will depart to deliver the packages.

        Returns:
            None

        Notes:
            time complexity:
                best case = O(n)
                worst case = O(n^2)
                average case = O(n^2)
            space complexity:
                best case = O(1)
                worst case = O(1)
                average case = O(1)
        """
        self.truck_status = "En Route"
        self.departure_time = departure_time

        # Loop through the packages the truck is carrying
        for i in self.packages:  # O(n) - for loop
            # Find the package in the package hash table and run the package_departure method
            data_structures_and_algorithms_ii.packages.get(i).package_departure(
                departure_time
            )  # O(n) - hash table get
