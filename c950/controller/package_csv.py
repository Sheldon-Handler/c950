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

import csv
from c950.hash.csv_handler import CsvHandler
from c950.__init__ import address_csv_file, package_csv_file, distance_csv_file


class PackageCsvController:
    """
    This class is a controller for the package csv file.

    Attributes:
        csv_handler (CsvHandler): A CsvHandler instance.
    """

    def __init__(self):
        """
        Initializes the PackageCsvController class.

        Args:
            csv_file ():
        """

    def read(self):
        """
        Gets all packages from the csv file.

        Returns:
            list: A list of all packages.
        """
        with open("./data/packages.csv") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            line_count = 0
            for row in csv_reader:
                print(row)
                line_count += 1
            print(f"Processed {line_count} lines.")

    def set(self):
        """
        Sets the csv file with the updated packages.

        """
        self.csv_handler.set()
        CsvHandler(package_csv_file, package_dao.get_packages())
