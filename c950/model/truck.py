"""This Python module defines a Truck class to represent a truck and its
information."""

#  MIT License
#
#  Copyright (c) 2023 Sheldon Handler
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice (including the next paragraph) shall be included in all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import dataclasses
import enum


class TruckStatus(enum.Enum):
    """Enum class to represent the status of a truck.

    Attributes:
        AT_HUB: Enum constant for truck at hub
        EN_ROUTE: Enum constant for truck en route
        RETURNING: Enum constant for truck returning
        FINISHED: Enum constant for truck finished

    Returns:
        TruckStatus: A TruckStatus Enum class instance.
    """

    AT_HUB = 0
    EN_ROUTE = 1
    RETURNING = 2
    FINISHED = 3


@dataclasses.dataclass
class Truck:
    """This dataclass represents a truck instance with its information.

    Attributes:
        id (int): The ID of the truck.
        truck_status (TruckStatus): The status of the truck.
        packages_assigned (list): The list of packages assigned for the truck to deliver.
        packages_loaded (list): The list of packages currently loaded onto the truck.
        packages_delivered (list): The list of packages delivered by the truck.

    Returns:
        Truck: A Truck class instance.
    """

    id: int
    truck_status: TruckStatus
    packages_assigned: list
    packages_loaded: list
    packages_delivered: list
