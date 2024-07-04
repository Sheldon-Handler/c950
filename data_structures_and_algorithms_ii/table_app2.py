#  MIT License
#
#  Copyright (c) 2024 Sheldon Handler
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice (including the next paragraph) shall be included in all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import tkinter


def packages_table(package_list: list, parent):
    root = parent
    root.title("Packages")

    # Define attribute names as labels in the first row
    package_column_names = package_list[0].__dict__.keys()
    package_column_names = list(package_column_names)

    package_cells = []

    for col, name in enumerate(package_column_names):
        label = tkinter.Label(root, text=name)
        label.grid(row=0, column=col)

    for i in range(len(package_list)):
        row_cells = []
        for j in range(len(package_column_names)):
            cell = tkinter.Label(
                root,
                text=getattr(package_list[i], package_column_names[j]),
                borderwidth=1,
                relief="solid",
                bg="white",
            )
            cell.grid(row=i + 1, column=j, sticky="nsew")
            row_cells.append(cell)
        package_cells.append(row_cells)


def addresses_table(address_list: list, parent):
    root = tkinter.Toplevel(parent)
    root.title("Addresses")

    # Define attribute names as labels in the first row
    address_column_names = address_list[0].__dict__.keys()
    address_column_names = list(address_column_names)

    address_cells = []

    for col, name in enumerate(address_column_names):
        label = tkinter.Label(root, text=name)
        label.grid(row=0, column=col)

    for i in range(len(address_list)):
        row_cells = []
        for j in range(len(address_column_names)):
            cell = tkinter.Label(
                root,
                text=getattr(address_list[i], address_column_names[j]),
                borderwidth=1,
                relief="solid",
                bg="white",
            )
            cell.grid(row=i + 1, column=j, sticky="nsew")
            row_cells.append(cell)
        address_cells.append(row_cells)


def trucks_table(truck_list: list, parent):
    root = tkinter.Toplevel(parent)
    root.title("Trucks")

    # Define attribute names as labels in the first row
    truck_column_names = truck_list[0].__dict__.keys()
    truck_column_names = list(truck_column_names)

    truck_cells = []

    for col, name in enumerate(truck_column_names):
        label = tkinter.Label(root, text=name)
        label.grid(row=0, column=col)

    for i in range(len(truck_list)):
        row_cells = []
        for j in range(len(truck_column_names)):
            cell = tkinter.Label(
                root,
                text=getattr(truck_list[i], truck_column_names[j]),
                borderwidth=1,
                relief="solid",
                bg="white",
            )
            cell.grid(row=i + 1, column=j, sticky="nsew")
            row_cells.append(cell)
        truck_cells.append(row_cells)
