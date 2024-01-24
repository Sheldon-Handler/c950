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


def load_package_csv(csv_file) -> list:
    """
    Loads the package csv file.

    Args:
        csv_file (str): The path to the csv file.

    Returns:
        list: A list of all packages.
    """

    # Declare a list to store packages converted from sublist.
    package_list = []

    # Read the csv file and store it in a variable.
    csvhandler = data_structures_and_algorithms_ii.hash.csv_handler.read(csv_file)

    for row in csvhandler:
        package_list.append(
            data_structures_and_algorithms_ii.model.package.Package(*row)
        )

    data_structures_and_algorithms_ii.packages = package_list

    return package_list
