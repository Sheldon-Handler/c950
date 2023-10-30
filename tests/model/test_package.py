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


class TestPackage(unittest.TestCase):
    def test_package(self):
        package = model.package.Package(
            1,
            "123 Main Street",
            "Salt Lake City",
            "UT",
            "84111",
            10,
            "EOD",
            "Some note",
            c950.c950.status.delivery_status.DeliveryStatus.AT_HUB,
        )
        self.assertEqual(package.id, 1)
        self.assertEqual(package.address, "123 Main Street")
        self.assertEqual(package.city, "Salt Lake City")
        self.assertEqual(package.state, "UT")
        self.assertEqual(package.zip, "84111")
        self.assertEqual(package.weight_kilo, 10)
        self.assertEqual(package.delivery_deadline, "EOD")
        self.assertEqual(package.special_notes, "Some note")
        self.assertEqual(
            package.delivery_status, model.delivery_status.DeliveryStatus.AT_HUB
        )


if __name__ == "__main__":
    unittest.main()
