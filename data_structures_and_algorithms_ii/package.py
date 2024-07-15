import datetime

import address
import hash_table
import __init__


class ModifiedTime:
    """This dataclass represents a modified time object with its information which has not had any data mutated."""

    def __init__(self, old_data, hour: int, minute: int):
        """
        Initializes a ModifiedTime class instance.

        Args:
            old_data: The old data before it was mutated.
            hour (int): The hour of the time.
            minute (int): The minute of the time.
        """
        self.old_data = old_data
        self.modified_time = datetime.time(hour, minute)

    def __str__(self) -> str:
        """Returns the string representation of the ModifiedTime object.

        Returns:
            str: The string representation of the ModifiedTime object.

        Notes:
            time complexity:
                best case: O(1)
                worst case: O(1)
                average case: O(1)
            space complexity:
                best case: O(1)
                worst case: O(1)
                average case: O(1)
        """
        return f"{self.modified_time}\n"


class Package:
    """This dataclass represents a package instance with its information which has not had any data mutated."""

    def __init__(
            self,
            id: int,
            address_id: int,
            address_name: str,
            address: str,
            city: str,
            state: str,
            zip: str,
            delivery_deadline: str,
            weight_kilo: int,
            special_notes: str,
            delivery_status: str = None,
            truck_id: int = None,
            arrival_time: datetime.time = datetime.time(hour=8, minute=0),
            load_time: datetime.time = None,
            departure_time: datetime.time = None,
            delivery_time: datetime.time = None,
            modified_time: ModifiedTime = None,
    ):
        """
        Initializes a Package class instance. Converts the string values to the appropriate data types.

        Args:
            id (int): The package id.
            address_id (int): The id of the address of the package.
            address_name (str): The name of the address.
            address (str): The package address.
            city (str): The package city.
            state (str): The package state.
            zip (str): The package zip code.
            delivery_deadline (datetime.time): The package delivery deadline.
            weight_kilo (int): The package weight in kilos.
            special_notes (str): The package special notes.
            delivery_status (str): The package delivery status.
            truck_id (int): The id of truck assigned to the package.
            arrival_time (datetime.time): The time when the package arrives at the hub.
            load_time (datetime.time): The time when the package is loaded onto the truck.
            departure_time (datetime.time): The time when the truck departs to deliver the package.
            delivery_time (datetime.time): The package delivery time.
            modified_time (ModifiedTime): The time the package was modified.
        """
        self.id = id
        self.address_id = address_id
        self.address_name = address_name
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.delivery_deadline = delivery_deadline
        self.weight_kilo = weight_kilo
        self.special_notes = special_notes
        self.delivery_status = delivery_status
        self.truck_id = truck_id
        self.arrival_time = arrival_time
        self.load_time = load_time
        self.departure_time = departure_time
        self.delivery_time = delivery_time
        self.modified_time = modified_time

    def update_address(self, correct_address_id: int, hour_modified, minute_modified) -> None:
        """
        Updates the address field to a corrected one.

        Args:
            correct_address_id (int): The correct address to replace existing address with.

        Returns:
            None

        Notes:
            time complexity:
                best case: O(1)
                worst case: O(1)
                average case: O(1)
            space complexity:
                best case: O(1)
                worst case: O(1)
                average case: O(1)
        """
        address_list = __init__.addresses

        correct_address: address.Address = None
        old_address: address.Address = None

        for i in address_list:
            if i.id == correct_address_id:
                correct_address = i

            if i.id == self.address_id:
                old_address = i

        self.address_id = correct_address.id
        self.address_name = correct_address.name
        self.address = correct_address.address

        self.modified_time = ModifiedTime(old_address, hour_modified, minute_modified)

    def update_delivery_status(self, updated_delivery_status: str) -> None:
        """Updates the delivery status of the package. If a delivery time is provided, it will also update the
        delivery time of the package.

        Args:
            updated_delivery_status (str): The delivery status to set for the package.

        Returns:
            None

        Notes:
            time complexity:
                best case: O(1)
                worst case: O(1)
                average case: O(1)
            space complexity:
                best case: O(1)
                worst case: O(1)
                average case: O(1)
        """
        self.delivery_status = updated_delivery_status
        print(f"Package {self.id} delivery status updated to {self.delivery_status}.\n")

    def set_arrival_time(self, arrival_time: datetime.time) -> None:
        """Sets the arrival time of the package.

        Args:
            arrival_time (datetime.time): The time when package arrives at the hub.

        Returns:
            None

        Notes:
            time complexity:
                best case: O(1)
                worst case: O(1)
                average case: O(1)
            space complexity:
                best case: O(1)
                worst case: O(1)
                average case: O(1)
        """
        self.delivery_status = "At Hub"
        self.arrival_time = arrival_time
        print(f"Package {self.id} arrived to hub at {self.arrival_time}.\n")

    def load_package(
            self, truck_id: int, load_time: datetime.time = datetime.time(hour=8, minute=2)
    ) -> None:
        """Loads the package onto the truck. Updates the truck_id attribute.

        Args:
            truck_id (int): The ID of the truck that will carry the package.
            load_time (datetime.time): The time that the package was loaded onto the truck. Defaults to 8:00 AM.

        Returns:
            None

        Notes:
            time complexity:
                best case: O(1)
                worst case: O(1)
                average case: O(1)
            space complexity:
                best case: O(1)
                worst case: O(1)
                average case: O(1)
        """
        self.truck_id = truck_id
        self.delivery_status = "At Hub"
        self.load_time = load_time
        print(f"Package {self.id} loaded onto truck {self.truck_id}.\n")

    def package_departure(self, departure_time: datetime.time) -> None:
        """Sends the truck to deliver the package. Updates departure_time and delivery_status attributes.

        Args:
            departure_time (datetime.time): The time the truck departs to deliver the package.

        Returns:
            None

        Notes:
            time complexity:
                best case: O(1)
                worst case: O(1)
                average case: O(1)
            space complexity:
                best case: O(1)
                worst case: O(1)
                average case: O(1)
        """
        self.departure_time = departure_time
        self.delivery_status = "En Route"
        print(
            f"Truck {self.truck_id} sent to deliver package {self.id} at {self.departure_time}.\n"
        )

    def deliver_package(self, delivery_time: datetime.time) -> None:
        """Delivers the package. Updates the delivery_status and delivery_time attributes.

        Args:
            delivery_time (datetime.time): The time that the package was delivered.

        Returns:
            None

        Notes:
            time complexity:
                best case: O(1)
                worst case: O(1)
                average case: O(1)
            space complexity:
                best case: O(1)
                worst case: O(1)
                average case: O(1)
        """
        self.delivery_status = "Delivered"
        self.delivery_time = delivery_time
        print(
            f"Package {self.id} delivered at {self.delivery_time} on truck {self.truck_id}.\n"
        )

    def __str__(self) -> str:
        """Returns the string representation of the Package object.

        Returns:
            str: The string representation of the Package object.

        Notes:
            time complexity:
                best case: O(1)
                worst case: O(1)
                average case: O(1)
            space complexity:
                best case: O(1)
                worst case: O(1)
                average case: O(1)
        """

        return (
            f"Package ID: {self.id}\n"
            f"Address ID: {self.address_id.__str__()}\n"
            f"City: {self.city}\n"
            f"State: {self.state}\n"
            f"Zip: {self.zip}\n"
            f"Delivery Deadline: {self.delivery_deadline}\n"
            f"Weight: {self.weight_kilo} kilos\n"
            f"Special Notes: {self.special_notes}\n"
            f"Delivery Status: {self.delivery_status}\n"
            f"Truck ID: {self.truck_id}\n"
            f"Arrival Time: {self.arrival_time}\n"
            f"Load Time: {self.load_time}\n"
            f"Departure Time: {self.departure_time}\n"
            f"Delivery Time: {self.delivery_time}\n"
        )


def get_package_ids_with_address_id(
        address_id: int,
        packages: hash_table.HashTable(),
) -> [int]:
    """
    This function returns a list of package ids whose address matches the address id.

    Args:
        address_id (int): id of the address to match.
        packages (list): list of packages to search through.

    Returns:
        [int]: list of package ids that match the address id.

    Notes:
        time complexity:
            best case: O(n)
            worst case: O(n)
            average case: O(n)
        space complexity:
            best case: O(n)
            worst case: O(n)
            average case: O(n)
    """
    item_values = [i[1] for i in packages]  # O(n) - list comprehension

    # Search for the address id in the packages and return the package id if found
    matching_packages = []
    for i in item_values:  # O(n) - for loop
        if i.address == address_id:
            matching_packages.append(i.id)

    return matching_packages
