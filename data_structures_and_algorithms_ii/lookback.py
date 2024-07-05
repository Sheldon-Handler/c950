#  MIT License
#
#  Copyright (c) 2024 Sheldon Handler
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice (including the next paragraph) shall be included in all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import datetime

import data_structures_and_algorithms_ii


def check_deliveries_at_time(start_time: datetime.time, end_time: datetime.time) -> []:
    """
    Checks the deliveries that are scheduled between the start and end times.

    Args:
        start_time (datetime.time): The start time.
        end_time (datetime.time): The end time.

    Returns:
        list: A list of deliveries that are scheduled between the start and end times.
    """

    packages_tuple = data_structures_and_algorithms_ii.packages.get_all()
    packages_list = [i[1] for i in packages_tuple]

    # Get the list of packages for the truck
    packages_not_available = []
    packages_at_hub = []
    packages_en_route = []
    packages_delivered = []

    for package in packages_list:
        if package.status == "Not Available":
            packages_not_available.append(package)
        elif package.status == "At Hub":
            packages_at_hub.append(package)
        elif package.status == "En Route":
            packages_en_route.append(package)
        elif package.status == "Delivered":
            packages_delivered.append(package)
