"""This module provides the Package class to store package information."""

#  MIT License
#
#  Copyright (c) 2023 Sheldon Handler
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice (including the next paragraph) shall be included in all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

import datetime
from dataclasses import dataclass


@dataclass
class Package:
    """This dataclass defines a package instance with its information.

    Attributes:
        id (int): The package id.
        address (str): The package address.
        city (str): The package city.
        state (str): The package state.
        zip (str): The package zip code.
        delivery_deadline (str): The package delivery deadline.
        weight_kilo (int): The package weight in kilos.
        special_notes (str): The package special notes.
        machine_readable_delivery_deadline (datetime.time): The package delivery deadline in a format that can be used
            for calculation of the delivery time.
        special_notes_attribute_key (str): The package special notes attribute key.
        special_notes_attribute_value (list or int or str or dict): The package special notes attribute value.
        delivery_status (str): The package delivery status.
        truck_id (int): The package delivery truck ID.
        delivery_time (str): The package delivery time.

    Returns:
        Package: A Package class instance.
    """

    id: int
    address: str
    city: str
    state: str
    zip: str
    delivery_deadline: str
    weight_kilo: int
    special_notes: str
    machine_readable_delivery_deadline: datetime.time = None
    special_notes_attribute_key: str = None
    special_notes_attribute_value: list or int or str = None
    delivery_status: str = None
    truck_id: int = None
    delivery_time: datetime.time = None

    def __post_init__(self):
        """Post initialization method to set the default values for the package instance.
        This method is called after the __init__ method in the dataclass.
        """
        # Handles the delivery deadline for the package.
        self.time_format()

        # Handles the special notes for the package.
        self.special_notes_handler()

    def special_notes_handler(self):
        """Handles the special notes for the package. Sets the special_notes_attribute_key and
        special_notes_attribute_value based on the special_notes attribute. This is done by parsing the special_notes
        string for the string prefix that defines the special note type.

        """

        # If there are no special notes
        if self.special_notes is None or self.special_notes == "":
            self.special_notes_attribute_key = ""
            self.special_notes_attribute_value = ""

        # If the special notes are "Can only be on truck {truck_id}"
        elif self.special_notes.startswith("Can only be on truck "):
            self.special_notes_attribute_key = "Can only be on truck"
            self.special_notes_attribute_value = int(
                self.special_notes.removeprefix("Can only be on truck ")
            )
            self.delivery_status = "At Hub"

        # If the special notes are "Delayed on flight---will not arrive to depot until {time}"
        elif self.special_notes.startswith(
            "Delayed on flight---will not arrive to depot until "
        ):
            self.special_notes_attribute_key = (
                "Delayed on flight---will not arrive to depot until"
            )
            self.delivery_status = "Not Available"
            self.special_notes_attribute_value = (
                self.special_notes.removeprefix(
                    "Delayed on flight---will not arrive to depot until "
                )
                .capitalize()
                .rstrip()
            )

        # If the special notes are "Wrong address listed"
        elif self.special_notes.startswith("Wrong address listed"):
            self.special_notes_attribute_key = "Wrong address listed"
            self.special_notes_attribute_value = self.address
            # Set the address to an empty string. This will be used to check if the address is correct.
            self.address = ""

        # If the special notes are "Must be delivered with {list(package_ids) as comma delimited values}"
        elif self.special_notes.startswith("Must be delivered with "):
            self.special_notes_attribute_key = "Must be delivered with"
            self.package_id_list = (
                self.special_notes.removeprefix("Must be delivered with ")
                .strip(" ")
                .split(",")
            )
            # Convert the package ids to integers
            self.special_notes_attribute_value = [
                int(package_id) for package_id in self.package_id_list
            ]

        else:
            raise ValueError("Invalid special notes value.")

    def time_format(self):
        """Takes the delivery_deadline attribute and formats it to save into the machine_readable_delivery_deadline
        attribute."""

        if self.delivery_deadline == "EOD":
            self.machine_readable_delivery_deadline = datetime.time(23, 59)

        self.machine_readable_delivery_deadline = datetime.datetime.strptime(
            self.delivery_deadline, "%I:%M %p"
        ).time()

    def update_address(self, correct_address: str):
        """Updates the address of the package to the correct address."""
        self.address = correct_address

    def update_delivery_status(self, delivery_status: str) -> bool:
        """Updates the delivery status of the package. If a delivery time is provided, it will also update the
        delivery time of the package.

        Args:
            delivery_status (str): The delivery status of the package.
        """

        if delivery_status == (
            "Not Available" or "At Hub" or "En Route" or "Delivered"
        ):
            self.delivery_status = delivery_status
            print(
                f"Package {self.id} delivery status updated to {self.delivery_status}.\n"
            )
            return True
        else:
            raise ValueError(
                "Invalid delivery status value. Please enter either one of the following:\n",
                "'Not Available'\n'At Hub'\n'En Route'\n'Delivered'\n",
            )

    def update_delivery_time(self, delivery_time: datetime.time) -> None:
        """Updates the delivery_time attribute of the package.

        Args:
            delivery_time (datetime.time): The time that the package was delivered.
        """

        self.delivery_time = delivery_time
        print(f"Package {self.id} delivery time updated to {self.delivery_time}.\n")
