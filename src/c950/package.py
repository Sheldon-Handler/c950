#  MIT License
#
#  Copyright (c) 2023 Sheldon Handler
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice (including the next paragraph) shall be included in all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


class Package:
    """This class represents a package object with attributes representing the
    details of the package.

    See Also:
        https://docs.python.org/3/library/dataclasses.html
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
        delivery_deadline: str,
        special_notes: str,
        delivery_status: str,
        delivery_time: str,
        delivery_truck: int,
    ):
        """Initialize the Package instance.

        Args:
            self (Package): The Package instance to initialize.
            package_id (int): The package ID.
            address (str): The package address.
            city (str): The package city.
            state (str): The package state.
            zip (str): The package zip code.
            weight_kilo (int): The package KILO weight.
            delivery_deadline (str): The package delivery deadline.
            special_notes (str): The package special notes.
            delivery_status (str): The package delivery status.
            delivery_time (str): The package delivery time.
            delivery_truck (int): The package delivery truck.

        Returns:
            Package: A Package instance.
        """

        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.weight_kilo = weight_kilo
        self.delivery_deadline = delivery_deadline
        self.special_notes = special_notes
        self.delivery_status = delivery_status
        self.delivery_time = delivery_time
        self.delivery_truck = delivery_truck

    def to_list(self):
        return [
            self.package_id,
            self.address,
            self.city,
            self.state,
            self.zip,
            self.weight_kilo,
            self.delivery_deadline,
            self.special_notes,
            self.delivery_status,
            self.delivery_time,
            self.delivery_truck,
        ]
