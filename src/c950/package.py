#  MIT License
#
#  Copyright (c) 2023 Sheldon Handler
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice (including the next paragraph) shall be included in all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import enum
import dataclasses
import time
from collections import namedtuple
from typing import overload

import truck


# Package dataclass to store package information.
#
# Args:
#     cls_name (str): The name of the class to create.
#     fields (list): A list of attributes representing the information to store in the class instance.
#
# Returns:
#     Package: A Package dataclass.


Package = dataclasses.make_dataclass(
    "Package",
    [
        ("package_id", int, dataclasses.field(hash=True)),
        ("address", str, dataclasses.field()),
        ("city", str, dataclasses.field()),
        ("state", str, dataclasses.field()),
        ("zip", str, dataclasses.field()),
        ("weight_kilo", int, dataclasses.field()),
        ("delivery_deadline", time, dataclasses.field()),
        ("special_notes", str, dataclasses.field()),
        ("delivery_status", DeliveryStatus, dataclasses.field()),
        ("delivery_truck", truck, dataclasses.field()),
        ("delivery_time", time, dataclasses.field()),
    ],
)


@overload
class Package:
    """This class represents a package to be delivered.

    Attributes:
        package_id (int): The package id.
        address (str): The package address.
        city (str): The package city.
        state (str): The package state.
        zip (str): The package zip code.
        weight_kilo (int): The package weight in kilos.
        delivery_deadline (time): The package delivery deadline.
        special_notes (str): The package special notes.
        delivery_status (DeliveryStatus): The package delivery status.
        delivery_truck (truck): The package delivery truck.
        delivery_time (time): The package delivery time.
    """

    # Constructor
    def __init__(
        self,
        package_id: int,
        address: str,
        city: str,
        state: str,
        zip: str,
        weight_kilo: int,
        delivery_deadline: time,
        special_notes: str,
        delivery_status: DeliveryStatus,
        delivery_truck: truck,
        delivery_time: time,
    ):
        """Initialize a Package object.

        Args:
            package_id (int): The ID of the package
            address (str): The address to delivery the package to.
            city (str): The city to delivery the package to.
            state (str): The state to delivery the package to.
            zip (str): The zip code to delivery the package to.
            weight_kilo (int): The weight of the package in KILO's.
            delivery_deadline (time): The deadline to deliver the package.
            special_notes (str): The special notes for the package delivery.
            delivery_status (DeliveryStatus): The delivery status of the package.
            delivery_truck (truck.Truck): The truck assigned to deliver the package
            delivery_time (time): The time that the package was delivered.
        """

        # Setting the attributes of the package
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.weight_kilo = weight_kilo
        self.delivery_deadline = delivery_deadline
        self.special_notes = special_notes
        self.delivery_status = delivery_status
        self.delivery_truck = delivery_truck
        self.delivery_time = delivery_time

    # String representation of the package
    def __str__(self):
        """This method returns the string representation of the package.

        Args:
            self (Package): The package to represent.

        Returns:
            str: A string representation of the package.
        """

        # Return the string representation of the package
        return f"Package ID: {self.package_id}, Address: {self.address}, City: {self.city}, State: {self.state}, Zip: {self.zip}, Weight: {self.weight_kilo}, Deadline: {self.delivery_deadline}, Notes: {self.special_notes}, Status: {self.delivery_status}, Truck: {self.delivery_truck}, Delivery Time: {self.delivery_time}"

    # Hash value of the package
    def __hash__(self):
        """This method returns the hash value of the package. The package ID is
        used as the hash value.

        Args:
            self (Package): The package to hash.

        Returns:
            int: The hash value of the package.
        """

        # Return the hash value of the package
        return hash(self.package_id)
