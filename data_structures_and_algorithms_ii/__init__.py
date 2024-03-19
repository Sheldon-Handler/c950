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
import fileinput
import os
import pathlib

import address
import deliver_together
import hash_table
import __main__
import nearest_neighbor
import package
import package_gui
import read_csv_file
import shell
import truck
import truck_loader

addresses = []
distances = []
packages = []
trucks = []
visited_location_indices = {}
unvisited_location_indices = {}
number_of_drivers = 2
number_of_trucks = 3
truck_capacity = 16
truck_speed = 18
starting_location = 0

address_csv_file = os.path.relpath("data/address.csv", start=os.pardir)
distance_csv_file = os.path.relpath("data/distance.csv", start=os.pardir)
package_csv_file = os.path.relpath("data/package.csv", start=os.pardir)
