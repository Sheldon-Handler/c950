import datetime
import data_structures_and_algorithms_ii


class Package:
    """This dataclass represents a package instance with its information which has not had any data mutated.

    Attributes:
        id (int): The package id.
        address (str): The package address.
        city (str): The package city.
        state (str): The package state.
        zip (str): The package zip code.
        delivery_deadline (datetime.time): The package delivery deadline.
        weight_kilo (int): The package weight in kilos.
        special_notes (str): The package special notes.
    """

    def __init__(
        self,
        id: int,
        address: str,
        city: str,
        state: str,
        zip: str,
        delivery_deadline: datetime.time,
        weight_kilo: int,
        special_notes: str,
    ):
        """
        Initializes a Package class instance. Converts the string values to the appropriate data types.

        Args:
            id (int): The package id.
            address (str): The package address.
            city (str): The package city.
            state (str): The package state.
            zip (str): The package zip code.
            delivery_deadline (datetime.time): The package delivery deadline.
            weight_kilo (int): The package weight in kilos.
            special_notes (str): The package special notes.
        """
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.delivery_deadline = delivery_deadline
        self.weight_kilo = weight_kilo
        self.special_notes = special_notes


class PackageAttributes:
    """This subclass defines the additional information for a package that. It inherits from the RawPackage class.

    Attributes:
        package (Package): The immutable raw package data associated with this package.
        correct_address (str): The correct package address.
        machine_readable_delivery_deadline (datetime.time): The package delivery deadline in a format that can be used
            for calculation of the delivery time.
        special_notes_attribute_key (str): The package special notes attribute key.
        special_notes_attribute_value (list or int or datetime.time): The package special notes attribute value.
        delivery_status (str): The package delivery status.
        truck_id (int): The package delivery truck ID.
        delivery_time (datetime.time): The package delivery time.

    Returns:
        PackageAttributes: A Package class instance.
    """

    package: Package
    correct_address: str
    machine_readable_delivery_deadline: datetime.time
    special_notes_attribute_key: str
    special_notes_attribute_value: list or int or datetime.time
    delivery_status: str
    truck_id: int
    delivery_time: datetime.time

    def __init__(self, package: Package):
        """
        Initializes a PackageAttributes class instance.

        Args:
            package (Package): The package data for this that are associated with these attributes.
        """
        self.package = package

        # Call the special_notes_handler method to handle the special notes for the package.
        self.special_notes_handler()

    def special_notes_handler(self):
        """Handles the special notes for the package. Translate special_notes to special_notes_attribute_key and
        special_notes_attribute_value to enable the program to handle the special notes.
        """

        # If there are no special notes
        if self.package.special_notes == "":
            self.special_notes_attribute_key = ""
            self.special_notes_attribute_value = ""

        # If the special notes are "Can only be on truck {truck_id}"
        elif self.package.special_notes.startswith("Can only be on truck "):
            self.special_notes_attribute_key = "Can only be on truck"
            self.special_notes_attribute_value = int(
                self.package.special_notes.removeprefix("Can only be on truck ")
            )
            self.delivery_status = "At Hub"

        # If the special notes are "Delayed on flight---will not arrive to depot until {time}"
        elif self.package.special_notes.startswith(
            "Delayed on flight---will not arrive to depot until "
        ):
            self.special_notes_attribute_key = (
                "Delayed on flight---will not arrive to depot until"
            )
            self.delivery_status = "Not Available"
            self.special_notes_attribute_value = (
                self.package.special_notes.removeprefix(
                    "Delayed on flight---will not arrive to depot until "
                )
                .capitalize()
                .rstrip()
            )

        # If the special notes are "Wrong address listed"
        elif self.package.special_notes.startswith("Wrong address listed"):
            self.special_notes_attribute_key = "Wrong address listed"
            # Store the incorrect address in the special_notes_attribute_value
            self.special_notes_attribute_value = self.package.address
            # Set the address to an empty string. This will be used to check if the address is correct.
            self.package.address = ""

        # If the special notes are "Must be delivered with {list(package_ids) as comma delimited values}"
        elif self.package.special_notes.startswith("Must be delivered with "):
            self.special_notes_attribute_key = "Must be delivered with"
            package_id_list = (
                self.package.special_notes.removeprefix("Must be delivered with ")
                .strip(" ")
                .split(",")
            )
            # Convert the package ids to integers
            self.special_notes_attribute_value = [
                int(package_id) for package_id in package_id_list
            ]

        else:
            raise ValueError("Invalid special notes value.")

    def update_delivery_status(self, delivery_status: str) -> bool:
        """Updates the delivery status of the package. If a delivery time is provided, it will also update the
        delivery time of the package.

        Args:
            delivery_status (str): The delivery status of the package.

        Returns:
            bool: True if the delivery status was updated successfully. False if the delivery status was not updated
                successfully.
        """

        # Check that the delivery_status is a valid value.
        if delivery_status == (
            "Not Available" or "At Hub" or "En Route" or "Delivered"
        ):
            self.delivery_status = delivery_status
            print(
                f"Package {self.package.id} delivery status updated to {self.delivery_status}.\n"
            )
            return True
        else:
            raise ValueError(
                "Invalid delivery status value. Please enter either one of the following:\n",
                "'Not Available'\n'At Hub'\n'En Route'\n'Delivered'\n",
            )

    def deliver(self, delivery_time: datetime.time = datetime.datetime.now().time()):
        """Delivers the package. Updates the delivery_status and delivery_time attributes.

        Args:
            delivery_time (datetime.time): The time that the package was delivered. Defaults to the current time.
        """
        self.update_delivery_status("Delivered")
        self.delivery_time = delivery_time
        print(f"Package {self.package.id} delivered at {self.delivery_time}.\n")
