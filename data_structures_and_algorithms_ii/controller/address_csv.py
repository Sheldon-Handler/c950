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

import csv

import data_structures_and_algorithms_ii


def read(file) -> list[data_structures_and_algorithms_ii.model.address.Address]:
    """
    This function reads a csv file and returns a list of Location objects.

    Args:
        file (): The file to read from.

    Returns:

    """
    list_of_locations = []

    csv_file = open(file, mode="r", newline="")
    reader = csv.reader(csv_file)

    for row in reader:
        list_of_locations.append(
            data_structures_and_algorithms_ii.model.address.Address(
                int(row[0]), row[1], row[2]
            )
        )

    csv_file.close()

    return list_of_locations


def write(
    file,
    list_of_locations,
) -> None:
    csv_file = open(file, mode="w", newline="")
    writer = csv.writer(csv_file)

    writer.writerows(list_of_locations.__dict__.values())

    csv_file.close()
