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


class DeliveryStatus(enum.Enum):
    """This enum class represents the delivery status of a package.

    Attributes:
        NOT_AVAILABLE (int): The package is not available.
        AT_HUB (int): The package is at the hub.
        EN_ROUTE (int): The package is en route.
        DELIVERED (int): The package has been delivered.

    See Also:
        https://docs.python.org/3/library/enum.html
    """

    NOT_AVAILABLE = 0
    AT_HUB = 1
    EN_ROUTE = 2
    DELIVERED = 3


@dataclasses.dataclass
class Package:
    """This class represents a package object with attributes representing the
    details of the package.

    Attributes:
        package_id (int): The package id.
        address (str): The package address.
        city (str): The package city.
        state (str): The package state.
        zip (str): The package zip code.
        weight_kilo (int): The package weight in kilos.
        delivery_deadline (time): The package delivery deadline.
        special_notes (str): The package special notes.
        delivery_status (str): The package delivery status.
        delivery_truck (int): The package delivery truck.
        delivery_time (time): The package delivery time.

    See Also:
        https://docs.python.org/3/library/dataclasses.html
        https://docs.python.org/3/library/time.html
    """

    package_id: int
    address: str
    city: str
    state: str
    zip: str
    weight_kilo: int
    delivery_deadline: time
    special_notes: str
    delivery_status: DeliveryStatus
    delivery_truck: int
    delivery_time: time
