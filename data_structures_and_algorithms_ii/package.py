"""This module provides the Package class to store package information."""
import dataclasses
#  MIT License
#
#  Copyright (c) 2024 Sheldon Handler
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice (including the next paragraph) shall be included in all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

import datetime

import data_structures_and_algorithms_ii


@dataclasses.dataclass(frozen=True, order=True)
class RawPackage:
    """This dataclass represents a package instance with its information which has not had any data mutated.

        Args:
            id (int): The package id.
            address (str): The package address.
            city (str): The package city.
            state (str): The package state.
            zip (str): The package zip code.
            delivery_deadline (str): The package delivery deadline.
            weight_kilo (int): The package weight in kilos.
            special_notes (str): The package special notes.
    """
    id: int
    address: str
    city: str
    state: str
    zip: str
    delivery_deadline: str
    weight_kilo: int
    special_notes: str


class Package:
    """This subclass defines the additional information for a package that. It inherits from the RawPackage class.

    Attributes:
        raw_package (RawPackage): The immutable raw package data associated with this package.
        machine_readable_delivery_deadline (datetime.time): The package delivery deadline in a format that can be used
            for calculation of the delivery time.
        special_notes_attribute_key (str): The package special notes attribute key.
        special_notes_attribute_value (list or int or str or dict): The package special notes attribute value.
        delivery_status (str): The package delivery status.
        truck_id (int): The package delivery truck ID.
        delivery_time (datetime.time): The package delivery time.

    Returns:
        Package: A Package class instance.
    """

    def __init__(self, raw_package: RawPackage, machine_readable_delivery_deadline: datetime.time = None,
                 special_notes_attribute_key: str = None,
                 special_notes_attribute_value: list or int or datetime.time = None, delivery_status: str = None,
                 truck_id: int = None, delivery_time: datetime.time = None):
        """
        Initializes a Package class instance.

        Args:
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
            delivery_time (datetime.time): The package delivery time.
        """

        self.raw_package = raw_package
        self.machine_readable_delivery_deadline = machine_readable_delivery_deadline
        self.special_notes_attribute_key = special_notes_attribute_key
        self.special_notes_attribute_value = special_notes_attribute_value
        self.delivery_status = delivery_status
        self.truck_id = truck_id
        self.delivery_time = delivery_time

        self.machine_readable_delivery_deadline_handler()
        self.special_notes_handler()

    def machine_readable_delivery_deadline_handler(self):
        """Handles the machine readable delivery deadline for the package. Translate the delivery_deadline to a
        machine_readable_delivery_deadline attribute to enable the program to handle the delivery deadline.
        """
        # Sets the machine_readable_delivery_deadline attribute.
        if self.raw_package.delivery_deadline == "EOD":
            self.machine_readable_delivery_deadline = None
        else:
            self.machine_readable_delivery_deadline = datetime.datetime.strptime(
                self.raw_package.delivery_deadline, "%I:%M %p"
            ).time()

    def special_notes_handler(self):
        """Handles the special notes for the package. Translate special_notes to special_notes_attribute_key and
        special_notes_attribute_value to enable the program to handle the special notes.

        """

        # If there are no special notes
        if self.raw_package.special_notes == "":
            self.special_notes_attribute_key = ""
            self.special_notes_attribute_value = ""

        # If the special notes are "Can only be on truck {truck_id}"
        elif self.raw_package.special_notes.startswith("Can only be on truck "):
            self.special_notes_attribute_key = "Can only be on truck"
            self.special_notes_attribute_value = int(
                self.raw_package.special_notes.removeprefix("Can only be on truck ")
            )
            self.delivery_status = "At Hub"

        # If the special notes are "Delayed on flight---will not arrive to depot until {time}"
        elif self.raw_package.special_notes.startswith(
            "Delayed on flight---will not arrive to depot until "
        ):
            self.special_notes_attribute_key = (
                "Delayed on flight---will not arrive to depot until"
            )
            self.delivery_status = "Not Available"
            self.special_notes_attribute_value = (
                self.raw_package.special_notes.removeprefix(
                    "Delayed on flight---will not arrive to depot until "
                )
                .capitalize()
                .rstrip()
            )

        # If the special notes are "Wrong address listed"
        elif self.raw_package.special_notes.startswith("Wrong address listed"):
            self.special_notes_attribute_key = "Wrong address listed"
            # Store the incorrect address in the special_notes_attribute_value
            self.special_notes_attribute_value = self.raw_package.address
            # Set the address to an empty string. This will be used to check if the address is correct.
            self.address = ""

        # If the special notes are "Must be delivered with {list(package_ids) as comma delimited values}"
        elif self.raw_package.special_notes.startswith("Must be delivered with "):
            self.special_notes_attribute_key = "Must be delivered with"
            package_id_list = (
                self.raw_package.special_notes.removeprefix("Must be delivered with ")
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
                f"Package {self.raw_package.id} delivery status updated to {self.delivery_status}.\n"
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
        print(f"Package {self.raw_package.id} delivered at {self.delivery_time}.\n")


def get_package_by_id(
    package_id: int,
    packages: list[Package] = data_structures_and_algorithms_ii.packages,
) -> Package:
    """Returns a package object by its id.

    Args:
        package_id (int): The id of the package to return.
        packages (list[Package]): A list of packages.

    Returns:
        Package: The package object with the id provided.

    Notes:
        time complexity: O(n)
        space complexity: O(1)
    """
    for package in packages:  # O(n)
        if package.raw_package.id == package_id:
            return package


def get_index_of_package_by_id(
    package_id: int,
    packages: list[Package] = data_structures_and_algorithms_ii.packages,
) -> int or None:
    """Returns the index of a package object by its id.

    Args:
        package_id (int): The id of the package to return.
        packages (list[Package]): A list of packages.

    Returns:
        int: The index of the package object with the id provided.

    Notes:
        time complexity: O(n)
        space complexity: O(1)
    """
    for package in packages:  # O(n)
        if package.raw_package.id == package_id:
            return packages.index(package)

    print(f"Package with id {package_id} not found.")
    return None
