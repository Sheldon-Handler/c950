#  MIT License
#
#  Copyright (c) 2023 Sheldon Handler
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice (including the next paragraph) shall be included in all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import unittest

from src import c950


class TestCsvHandler(unittest.TestCase):
    def test_write(self):
        csv_handler = c950.controller.csv_handler.CsvHandler(
            filename="../resources/data/test.csv",
            header=[
                "package_id",
                "address",
                "city",
                "state",
                "zip_code",
                "weight",
                "deadline",
                "note",
                "status",
            ],
        )

        csv_handler.write(
            [
                [
                    1,
                    "123 Main Street",
                    "Salt Lake City",
                    "UT",
                    "84111",
                    10,
                    "EOD",
                    "Some note",
                    c950.model.delivery_status.DeliveryStatus.AT_HUB,
                ],
                [
                    2,
                    "123 Main Street",
                    "Salt Lake City",
                    "UT",
                    "84111",
                    10,
                    "EOD",
                    "Some note",
                    c950.model.delivery_status.DeliveryStatus.DELIVERED,
                ],
            ]
        )

        with open("../resources/data/test.csv", "r") as file:
            data = file.readlines()
            self.assertEqual(
                data[0],
                "package_id,address,city,state,zip_code,weight,deadline,note,status\n",
            )
            self.assertEqual(
                data[1],
                "1,123 Main Street,Salt Lake City,UT,84111,10,EOD,Some note,AT_HUB\n",
            )
            self.assertEqual(
                data[2],
                "2,123 Main Street,Salt Lake City,UT,84111,10,EOD,Some note,DELIVERED\n",
            )

    def test_read(self):
        csv_handler = c950.controller.csv_handler.CsvHandler(
            "../resources/data/test.csv",
            header=[
                "package_id",
                "address",
                "city",
                "state",
                "zip",
                "weight_kilo",
                "deadline",
                "note",
                "status",
            ],
        )

        self.assertEqual(
            csv_handler.read(),
            [
                [
                    "1",
                    "123 Main Street",
                    "Salt Lake City",
                    "UT",
                    "84111",
                    "10",
                    "EOD",
                    "Some note",
                    c950.model.delivery_status.DeliveryStatus.AT_HUB,
                ],
                [
                    "2",
                    "123 Main Street",
                    "Salt Lake City",
                    "UT",
                    "84111",
                    "10",
                    "EOD",
                    "Some note",
                    c950.model.delivery_status.DeliveryStatus.DELIVERED.name,
                ],
            ],
        )


if __name__ == "__main__":
    unittest.main()
