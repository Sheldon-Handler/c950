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

from csv_handler import CsvHandler

from c950.model.location import Location


def get_location_list():
    """Returns a list of locations from the location.csv file in ../data/locations.csv"""

    csv_handler = CsvHandler("../data/locations.csv")
    locations = csv_handler.read()

    for location in locations:
        location = Location(location[0], location[1], location[2])


class AddressDao(CsvHandler):
    def __init__(self, csv_file):
        super().__init__(csv_file)
        self.data = self.read()


def setall(csv_hand):
    """Sets all locations in the location table in the 'identifier.sqlite' database.

    Returns:
        None
    """

    csv_handler = CsvHandler("../data/locations.csv")
    csv_handler.read()
