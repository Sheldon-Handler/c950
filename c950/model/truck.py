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
#


from dataclasses import dataclass
from enum import Enum
from datetime import datetime

from package import Package, DeliveryStatus


class TruckStatus(Enum):
    """This enum represents the status of a truck.

    Attributes:
        NOT_AVAILABLE (int): The truck is not available.
        AT_HUB (int): The truck is at the hub.
        EN_ROUTE (int): The truck is en route.
        RETURNING (int): The truck is returning to the hub.

    Returns:
        TruckStatus: A TruckStatus enum instance.
    """

    NOT_AVAILABLE = 0
    AT_HUB = 1
    EN_ROUTE = 2
    RETURNING = 3


@dataclass
class Truck:
    """This dataclass represents a truck instance with its information.

    Attributes:
        id (int): The ID of the truck.
        truck_status (TruckStatus): The status of the truck.

    Returns:
        Truck: A Truck class instance.
    """

    id: int
    truck_status: TruckStatus
    address: str
    left_hub: datetime.time
    addresses_assigned: list
    packages_loaded: list
    packages_delivered: list

    def load_package(self, package: Package) -> None:
        """This method loads packages onto the truck.

        Args:
            packages (list): The list of packages to load onto the truck.

        Returns:
            None
        """

        # set the truck status to en route
        package.truck = self.id
        package.delivery_status = DeliveryStatus.EN_ROUTE
        package.loaded_time = datetime.now()
        self.packages_loaded.append(package)

    def deliver_package(self, package: Package) -> None:
        """This method delivers packages from the truck.

        Args:
            package (Package): The package to deliver from the truck.

        Returns:
            None
        """

        package.delivery_status = DeliveryStatus.DELIVERED
        package.delivery_time = datetime.now()
        self.packages_delivered.append(package)
