import datetime

import data_structures_and_algorithms_ii
import data_structures_and_algorithms_ii.address
import data_structures_and_algorithms_ii.delivery_time_calculator
import data_structures_and_algorithms_ii.nearest_neighbor
import data_structures_and_algorithms_ii.package


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
        truck_time: datetime.time = None,
        current_address: int = 0,
        # load_time: datetime.time = None,
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
        self.packages_delivered = []
        self.departure_time = departure_time
        self.truck_time = truck_time
        self.return_time = None
        self.visited_addresses = [0]
        self.traveled_distances = []
        self.current_address = current_address
        self.addresses_not_in_this_truck = []
        self.addresses_not_yet_delivered = []

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

    def load_truck(
        self,
        package_id: int,
        load_time: datetime.time = datetime.time(hour=8, minute=2),
    ) -> None:
        """Loads a package onto the truck.

        Args:
            package_id (int): The ID of the package to load onto the truck.
            load_time (datetime.time): The time the package is loaded onto the truck.

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
        package.load_package(self.id, load_time)
        # Add the package ID to the truck's packages list
        self.packages.append(package_id)
        # Add the address ID to list of addresses
        if package.address_id not in self.addresses:  # O(n) - list search
            self.addresses.append(package.address_id)
            self.addresses_not_yet_delivered.append(package.address_id)
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
        self.truck_time = departure_time

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
        Sorts the addresses by distance from the current address.

        Returns:
            [int]: address ID values sorted by distance from current address

        Notes:
            time complexity:
                best case = O(n^2 log n)
                worst case = O(n^2 log n)
                average case = O(n^2 log n)
            space complexity:
                best case = O(n)
                worst case = O(n)
                average case = O(n)
        """
        sorted_addresses = data_structures_and_algorithms_ii.nearest_neighbor.sorted_unvisited_neighbors(  # O(n^2 log n)
            data_structures_and_algorithms_ii.distances[self.current_address],
            (self.addresses_not_in_this_truck + self.visited_addresses),
        )

        return sorted_addresses

    def nearest_address(self) -> int:
        """

        Returns:
            int: ID of Address closes to current location

        """
        return self.sort_addresses()[0]

    def return_truck(self):
        """
        Brings the truck back to the hub.

        Returns:
            None

        Notes:
            time complexity:
                best case = O(n)
                worst case = O(n)
                average case = O(n)
            space complexity:
                best case = O(1)
                worst case = O(1)
                average case = O(1)
        """
        distance_between = data_structures_and_algorithms_ii.distances[
            self.current_address
        ][0]
        self.truck_time = (
            data_structures_and_algorithms_ii.delivery_time_calculator.time_updater(
                self.truck_time,
                distance_between,
            )  # O(n) - function call
        )
        self.return_time = self.truck_time
        self.traveled_distances.append(distance_between)
        self.distance_traveled += distance_between
        self.current_address = 0
        self.truck_status = "At Hub"
        print(f"Truck {self.id} has returned to the hub at {self.truck_time}.\n")

    def deliver(self, address_id: int) -> None:
        """
        Delivers a package to an address.

        Args:
            address_id (int): ID of the address to deliver.

        Returns:
            None

        Notes:
            time complexity:
                best case = O(n^3)
                worst case = O(n^3)
                average case = O(n^3)
            space complexity:
                best case = O(n)
                worst case = O(n)
                average case = O(n)
        """

        distance_between = data_structures_and_algorithms_ii.distances[
            self.current_address
        ][address_id]

        delivery_time = (
            data_structures_and_algorithms_ii.delivery_time_calculator.time_updater(
                self.truck_time, distance_between
            )
        )

        package_list = (
            data_structures_and_algorithms_ii.packages.get_all()
        )  # O(n^2) - function call
        item_values = [i[1] for i in package_list]  # O(n) - list comprehension

        # Loop through the package IDs to deliver the package
        for i in item_values:  # O(n) - for loop
            if i.address_id == address_id:
                if i.id in self.packages:  # O(n) - list search
                    data_structures_and_algorithms_ii.packages.get(
                        i.id  # O(n) - hash table get
                    ).deliver_package(delivery_time)
                    self.packages_delivered.append(i.id)

        # Update the truck's distance traveled
        added_distance = data_structures_and_algorithms_ii.distances[
            self.current_address
        ][address_id]
        self.traveled_distances.append(added_distance)
        self.distance_traveled += added_distance

        # Update the truck's truck time
        self.truck_time = delivery_time

        # Update the truck's current address
        self.current_address = address_id

        # Update the truck's visited addresses
        self.visited_addresses.append(address_id)

        # Update the truck's addresses not in this truck
        self.addresses_not_yet_delivered.remove(address_id)  # O(n) - list remove

    def deliver_all(self):
        """
        Delivers all packages in the truck.

        Returns:
            None

        Notes:
            time complexity:
                best case = O(n)
                worst case = O(n)
                average case = O(n^2)
            space complexity:
                best case = O(1)
                worst case = O(1)
                average case = O(1)
        """
        while len(self.addresses_not_yet_delivered) > 0:  # O(n) - while loop
            self.deliver(self.nearest_address())

        self.return_truck()


class TruckView:
    """
    This class represents a view of the truck at a given time
    """

    def __init__(
        self,
        truck_id: int,
        distance_traveled_at_time: float,
        distance_traveled_by_end_of_day: float,
        truck_status: str,
    ):
        """
        Initializes the TruckView class with the truck ID and distance traveled.

        Args:
            truck_id (int): The ID of the truck to create a view for.
            distance_traveled_at_time (float): The distance the truck has traveled at the given time.
            truck_status (str): The status of the truck.
        """
        self.truck_id = truck_id
        self.distance_traveled_at_time = distance_traveled_at_time
        self.distance_traveled_by_end_of_day = distance_traveled_by_end_of_day
        self.truck_status = truck_status


class TotalDistances:
    """
    This class represents the total distances traveled by the trucks.
    """

    def __init__(
        self,
        total_distance_traveled_at_time: float,
        total_distance_traveled_by_end_of_day: float,
    ):
        """
        Initializes the TotalDistances class with the total distances traveled by the trucks.

        Args:
            total_distance_traveled_at_time (float): The total distance traveled by the trucks at the given time.
            total_distance_traveled_by_end_of_day (float): The total distance traveled by the trucks by the end of the day.
        """
        self.total_distance_traveled_at_time = total_distance_traveled_at_time
        self.total_distance_traveled_by_end_of_day = (
            total_distance_traveled_by_end_of_day
        )
