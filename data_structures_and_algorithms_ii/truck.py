import datetime

import data_structures_and_algorithms_ii
import data_structures_and_algorithms_ii.address
import data_structures_and_algorithms_ii.nearest_neighbor


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
        departure_time: datetime.time = None,
        truck_time: datetime.timedelta = None,
        current_address: int = 0,
    ):
        """
        Initializes the truck class with its information.

        Args:
            id: The ID of the truck.
            truck_status: The status of the truck.
            distance_traveled: The distance the truck has traveled.
        """
        self.id = id
        self.truck_status = truck_status
        self.distance_traveled = distance_traveled
        self.packages = []
        self.addresses = [0]
        self.departure_time = departure_time
        self.truck_time = truck_time
        self.visited_addresses = [0]
        self.current_address = current_address
        self.addresses_not_in_this_truck = None

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
        # Add the package ID to the truck's packages list
        self.packages.append(package_id)
        # Add the address ID to list of addresses
        self.addresses.append(package.address)

        # Update the package in the package hash table
        data_structures_and_algorithms_ii.packages.update(
            package_id, package
        )  # O(n) - hash table update

    def depart_truck(self, departure_time: datetime.time):
        """Sends the truck to deliver the packages. Updates departure_time and delivery_status attributes of the
        packages in the truck.

        Args:
            departure_time (datetime.time): The time that the truck will depart to deliver the packages.

        Returns:
            None

        Notes:
            time complexity:
                best case = O(n^2)
                worst case = O(n^2)
                average case = O(n^2)
            space complexity:
                best case = O(1)
                worst case = O(1)
                average case = O(1)
        """
        self.truck_status = "En Route"
        self.departure_time = departure_time
        self.truck_time = datetime.timedelta(
            hours=departure_time.hour, minutes=departure_time.minute
        )

        # Loop through the packages the truck is carrying
        for i in self.packages:  # O(n) - for loop
            # Update the package in the package hash table
            data_structures_and_algorithms_ii.packages.get(i).package_departure(
                departure_time
            )  # O(n) - hash table get

        # Find addresses not in this truck
        self.addresses_not_in_this_truck = []
        for address in data_structures_and_algorithms_ii.addresses:  # O(n) - for loop
            if address.id not in self.addresses:
                self.addresses_not_in_this_truck.append(address.id)

    def sort_addresses(self) -> [int]:
        """


        Returns:
            [int]: address ID values sorted by distance from current address

        """

        #        excluded_addresses = self.addresses_not_in_this_truck + self.visited_addresses
        sorted_addresses = data_structures_and_algorithms_ii.nearest_neighbor.sorted_unvisited_neighbors(
            data_structures_and_algorithms_ii.distances[self.current_address],
            (self.addresses_not_in_this_truck + self.visited_addresses),
        )

        print(sorted_addresses)

        return sorted_addresses

    def nearest_address(self) -> int:
        """

        Returns:
            int: ID of Address closes to current location

        """
        return self.sort_addresses()[0]

    def deliver(self, package_id: int, delivery_time: datetime.time):
        """

        Args:
            package_id (int): ID of the package to deliver.
            delivery_time (datetime.time): The time of delivery for the package.

        Returns:

        """
        nearest_address = data_structures_and_algorithms_ii.nearest_neighbor.sorted_unvisited_neighbors(
            data_structures_and_algorithms_ii.distances[self.current_address],
            (self.addresses_not_in_this_truck, self.visited_addresses),
        )

        while len(self.packages) > 0:

            package = data_structures_and_algorithms_ii.packages.get(package_id)
            package.deliver_package(delivery_time)
