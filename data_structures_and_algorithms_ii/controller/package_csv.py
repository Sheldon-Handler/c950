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
from data_structures_and_algorithms_ii.model.package import Package


def read(file) -> list[Package]:
    """
    This function reads a csv file and returns a list of Location objects.

    Args:
        file (str): The file to read from.

    Returns:

    """
    packages = []

    csv_file = open(file, mode="r", newline="")
    reader = csv.reader(csv_file)

    for row in reader:
        packages.append(Package(*row))

    csv_file.close()

    return packages


def write(file, packages) -> None:
    """
    This function writes a list of Location objects to a csv file.

    Args:
        file (str): The file to write to.
        packages (list[Package]): The list of package objects to write.

    Returns:

    """

    csv_file = open(file, mode="w", newline="")
    writer = csv.writer(csv_file)

    writer.writerows(packages.__dict__.values())

    csv_file.close()
