"""This module provides the Package class to store package information."""
import dataclasses

#  MIT License
#
#  Copyright (c) 2023 Sheldon Handler
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice (including the next paragraph) shall be included in all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


import time
from enum import Enum
from dataclasses import dataclass
from truck import Truck
from address import Address


class DeliveryStatus(Enum):
    """This enum represents the delivery status of a package.

    Attributes:
        NOT_AVAILABLE (int): The package is not available.
        AT_HUB (int): The package is at the hub.
        EN_ROUTE (int): The package is en route.
        DELIVERED (int): The package has been delivered.

    Returns:
        DeliveryStatus: A DeliveryStatus enum instance.
    """

    NOT_AVAILABLE = 0
    AT_HUB = 1
    EN_ROUTE = 2
    DELIVERED = 3


@dataclass
class Package:
    """This dataclass defines a package instance with its information.

    Attributes:
        id (int): The package id.
        address (Address): The package location.
        city (str): The package city.
        state (str): The package state.
        zip (int): The package zip code.
        delivery_deadline (time): The package delivery deadline.
        weight_kilo (int): The package weight in kilos.
        special_notes (str): The package special notes.
        delivery_status (DeliveryStatus): The package delivery status.
        truck_id (int): The id of the package delivery truck.
        delivery_time (time): The package delivery time.

    Returns:
        Package: A Package class instance.
    """

    id: int
    address: Address
    city: str
    state: str
    zip: int
    delivery_deadline: time
    weight_kilo: int
    special_notes: str
    delivery_status: DeliveryStatus
    truck_id: int
    loaded_time: time
    delivery_time: time
