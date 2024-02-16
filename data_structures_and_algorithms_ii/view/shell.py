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

import argparse
import data_structures_and_algorithms_ii


class Shell:
    """
    This class is the command line interface for the package delivery service.

    Attributes:
        parser (ArgumentParser): The argument parser for the command line interface.

    Returns:
        Shell: A Shell class instance.

    Notes:
        time complexity: O(1)
        space complexity: O(1)
    """

    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Package Delivery Service")
        self.parser.add_argument(
            "-d",
            "--debug",
            help="Show debug information",
            action="store_true",
            required=False,
        )

    def correct_address(self, package_id, correct_address) -> None:
        """
        Updates the address of a package.

        Args:
            package_id (int): The id of the package to update.
            correct_address (str): The correct address for the package.

        Notes:
            time complexity: O(n)
            space complexity: O(1)
        """
        # Get the package by its id, then modify its address
        data_structures_and_algorithms_ii.model.package.get_package_by_id(
            package_id
        ).address = correct_address
