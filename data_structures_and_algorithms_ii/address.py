import datetime


class Address:
    """Represents an address object with its information."""

    def __init__(
        self,
        id: int,
        name: str,
        address: str,
        packages: [int],
        delivery_status: str = None,
        truck_id: int = None,
        departure_time: datetime.time = None,
        delivery_time: datetime.time = None,
    ):
        """
        Initializes an Address object instance with its information.

        Args:
            id (int): The id of the location.
            name (str): The name of the location.
            address (str): The address.
        """

        self.id = id
        self.name = name
        self.address = address
        self.delivery_status = delivery_status
        self.truck_id = truck_id
        self.departure_time = departure_time
        self.delivery_time = delivery_time

    def __str__(self):
        """Returns the string representation of the Address object."""
        return (
            f"ID: {self.id}, Name: {self.name}, Address: {self.address}, Delivery Status: {self.delivery_status}, "
            f"Truck ID: {self.truck_id}, Departure Time: {self.departure_time}, Delivery Time: {self.delivery_time}"
        )

    def load_address(self, package_id: int, truck_id: int) -> bool:
        """Loads a package onto a truck.

        Args:
            package_id (int): The ID of the package.
            truck_id (int): The ID of the truck.

        Returns:
            bool: True if the address was loaded successfully. False if the address was not loaded successfully.
        """
        self.delivery_status = "At Hub"
        package_id = package_id
        self.truck_id = truck_id
        return True

    def address_departure(self, departure_time: datetime.time) -> bool:
        """Sends the truck to deliver the package.

        Args:
            departure_time (datetime.time): The departure time of the truck.

        Returns:
            bool: True if the truck was sent to deliver the package successfully. False if the truck was not sent to
            deliver the package successfully.
        """
        self.delivery_status = "En Route"
        self.departure_time = departure_time
        return True

    def deliver_address(self, delivery_time: datetime.time) -> bool:
        """Delivers to the address.

        Args:
            delivery_time (datetime.time): The delivery time of the package.

        Returns:
            bool: True if the package was delivered successfully. False if the package was not delivered successfully.
        """
        self.delivery_status = "Delivered"
        self.delivery_time = delivery_time
        return True
