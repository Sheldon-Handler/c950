"""This Python module defines a Truck class to represent a truck and its
information."""

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

import dataclasses

import data_structures_and_algorithms_ii


@dataclasses.dataclass
class Truck:
    """This dataclass represents a truck instance with its information.

    Attributes:
        id (int): The ID of the truck.
        truck_status (TruckStatus): The status of the truck.
        distance_traveled (float): The distance the truck has traveled.
        packages (list[int]): The list of package IDs the truck is carrying.
        packages_delivered (list[int]): The list of package IDs the truck has delivered.

    Returns:
        Truck: A Truck class instance.
    """

    id: int
    truck_status: str
    distance_traveled: float = None
    packages: list[int] = None
    packages_delivered: list[int] = None

    def update_truck_status(self, truck_status: str) -> bool:
        """Updates the truck status.

        Args:
            truck_status (TruckStatus): The status of the truck.

        Returns:
            bool: True if the truck_status is valid and updated accordingly. Otherwise, raises a ValueError.
        """

        truck_statuses = ["Not Available", "At Hub", "En Route", "Returning"]

        if truck_status in truck_statuses:
            self.truck_status = truck_status
            print(f"Truck {self.id} status updated to {self.truck_status}.")
            return True
        else:
            raise ValueError(
                f"Truck status must be one of the following: {truck_statuses}."
            )


def get_truck_by_id(
    truck_id,
    trucks=data_structures_and_algorithms_ii.trucks,
) -> Truck:
    """Gets a truck by its ID.

    Args:
        truck_id (int): The ID of the truck to get.
        trucks (list): A list of Truck objects.

    Returns:
        Truck: The truck with the specified ID.
    """
    for truck in trucks:
        if truck.id == truck_id:
            return truck

    raise ValueError("Truck with id {} not found.".format(truck_id))


def get_index_of_truck_by_id(
    truck_id,
    trucks=data_structures_and_algorithms_ii.trucks,
) -> int or None:
    """Gets the index of a truck by its ID.

    Args:
        truck_id (int): The ID of the truck to get.
        trucks (list): A list of Truck objects.

    Returns:
        int: The index of the truck with the specified ID.
    """
    for truck in trucks:
        if truck.id == truck_id:
            return trucks.index(truck)

    print("Truck with id {} not found.".format(truck_id))
    return None
