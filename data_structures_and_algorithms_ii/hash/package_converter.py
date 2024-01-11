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

import data_structures_and_algorithms_ii

import datetime


def convert_to_csv_list(
    package,
):
    """Takes a Package object and converts it to a list of strings.

    Args:
        package (Package): Package to convert to a list for saving it in a csv file.

    Returns:

    """

    csv_list = [
        str(package.id),
        str(package.address),
        str(package.city),
        str(package.state),
        str(package.zip),
        str(package.delivery_deadline),
        str(package.weight_kilo),
        str(package.special_notes),
    ]
    return csv_list


def convert_to_package(package):
    """

    Args:
        package ():

    Returns:

    """

    new_package = data_structures_and_algorithms_ii.model.package.Package(
        id=int(package[0]),
        address=str(package[1]),
        city=str(package[2]),
        state=str(package[3]),
        zip=str(package[4]),
        delivery_deadline=datetime.time(package[5]),
        weight_kilo=int(package[6]),
        special_notes=str(package[7]),
        delivery_status=(package[8]),
        truck_id=int(package[9]),
        delivery_time=datetime.time(package[10]),
    )

    return new_package
