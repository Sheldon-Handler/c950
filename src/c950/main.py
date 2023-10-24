"""This module defines the main function for the program."""

#  MIT License
#
#  Copyright (c) <year> <fullname>
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

from package_dao import PackageDAO
import package

print("Hello, World!")

# new_item = Package(
#     1,
#     "123 Main Street",
#     "Salt Lake City",
#     "UT",
#     "84111",
#     10,
#     "EOD",
#     "Some note",
#     "AT_HUB",
# )

new_status = package.DeliveryStatus.NOT_AVAILABLE
print(new_status)

new_package = package.Package(
    package_id=1,
    address="123 Main Street",
    city="Salt Lake City",
    state="UT",
    zip="84111",
    weight_kilo=10,
    delivery_deadline="EOD",
    special_notes="Some note",
    delivery_status="AT_HUB",
    delivery_truck=None,
    delivery_time=None,
)


new_package.delivery_status = package.DeliveryStatus.AT_HUB
