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
from c950.model.package import Package
from c950.defaults import *


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
    truck_status: str
    route: list = None
    distance_traveled: float = None
    packages: list[int] = None

    def update_truck_status(self, truck_status: str) -> None:
        """Updates the truck status.

        Args:
            truck_status (TruckStatus): The status of the truck.
        """
        if truck_status in ["At Hub", "En Route", "Returning", "at location"]:
            self.truck_status = truck_status

    def load_package(self, package: Package) -> None:
        """Loads a package onto a truck.

        Args:
            package_id (int): The ID of the package to load onto the truck.
        """
        package.load_onto_truck(self.id)
        self.packages.append(package.id)
