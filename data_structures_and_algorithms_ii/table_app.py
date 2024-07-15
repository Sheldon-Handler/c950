#  MIT License
#
#  Copyright (c) 2024 Sheldon Handler
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice (including the next paragraph) shall be included in all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
import datetime
import tkinter

import data_structures_and_algorithms_ii.truck


def main_window(
    packages_list: list,
    trucks_view_list: list,
    hour: int,
    minute: int,
    total_distance_at_time: float,
    total_distance_by_end_of_day: float,
):
    """
    Creates the main window with the tables of packages and trucks

    Args:
        packages_list (list): A list of packages to display in the table.
        trucks_view_list (list): A list of truck view to display in the table.
        hour (int): The hour to display in the title.
        minute (int): The minute to display in the title

    Returns:
        None
    """
    # Create the main window
    root = tkinter.Tk()  # O(n) - Tk

    root.title("Packages at " + datetime.time(hour, minute).strftime("%I:%M %p"))

    packages_table(packages_list, root)  # O(n^3) - packages_table
    trucks_distance(trucks_view_list, root)  # O(n^3) - trucks_distance
    total_distances(
        root, total_distance_at_time, total_distance_by_end_of_day
    )  # O(n) - total_distances

    root.mainloop()


def packages_table(package_list: list, parent: tkinter.Tk) -> None:
    """
    Creates a table of packages.

    Args:
        package_list (list): A list of packages to display in the table.
        parent (tkinter.Tk): The parent window.

    Returns:
        None

    Notes:
        time complexity:
            best case: O(n^3)
            worst case: O(n^3)
            average case: O(n^3)
        space complexity:
            best case: O(n^3)
            worst case: O(n^3)
            average case: O(n^3)
    """
    root = tkinter.PanedWindow(parent)
    root.pack(fill="both", expand=1)  # O(n) - pack

    # Define attribute names as labels in the first row
    package_column_names = package_list[0].__dict__.keys()
    package_column_names = list(package_column_names)

    package_cells = []

    for col, name in enumerate(package_column_names):  # O(n) - for loop
        label = tkinter.Label(root, text=name)
        label.grid(row=0, column=col)

    for i in range(len(package_list)):  # O(n) - for loop
        row_cells = []
        for j in range(len(package_column_names)):  # O(n) - for loop
            cell = tkinter.Label(
                root,
                text=getattr(
                    package_list[i], package_column_names[j]
                ),  # O(n) - get attribute
                borderwidth=1,
                relief="solid",
                bg="white",
            )
            cell.grid(row=i + 1, column=j, sticky="nsew")
            row_cells.append(cell)
        package_cells.append(row_cells)


def trucks_distance(
    truck_view_list: [data_structures_and_algorithms_ii.truck.TruckView],
    parent: tkinter.Tk,
) -> None:
    """
    Creates a table of trucks and their distances traveled.

    Args:
        truck_view_list (data_structures_and_algorithms_ii.truck.TruckView): A list of TruckView objects.
        parent (tkinter.Tk): The parent window.

    Returns:
        None

    Notes:
        time complexity:
            best case: O(n^3)
            worst case: O(n^3)
            average case: O(n^3)
        space complexity:
            best case: O(n^3)
            worst case: O(n^3)
            average case: O(n^3)
    """
    root = tkinter.PanedWindow(parent)  # O(n) - PanedWindow
    root.pack(fill="both", expand=1)  # O(n) - pack

    # Define attribute names as labels in the first row
    truck_column_names = truck_view_list[0].__dict__.keys()  # O(n) - get keys
    truck_column_names = list(truck_column_names)  # O(n) - list conversion

    truck_cells = []

    for col, name in enumerate(truck_column_names):  # O(n) - for loop
        label = tkinter.Label(root, text=name)
        label.grid(row=0, column=col)

    for i in range(len(truck_view_list)):  # O(n) - for loop
        row_cells = []
        for j in range(len(truck_column_names)):  # O(n) - for loop
            cell = tkinter.Label(
                root,
                text=getattr(
                    truck_view_list[i], truck_column_names[j]
                ),  # O(n) - get attribute
                borderwidth=1,
                relief="solid",
                bg="white",
            )
            cell.grid(row=i + 1, column=j, sticky="nsew")
            row_cells.append(cell)
        truck_cells.append(row_cells)


def total_distances(
    parent: tkinter.Tk,
    total_distance_at_time: float,
    total_distance_by_end_of_day: float,
) -> None:
    """
    Calculates the total distance traveled by the trucks.

    Args:
        parent (tkinter.Tk): The parent window.
        total_distance_at_time (float): The total distance traveled by the trucks at the given time.
        total_distance_by_end_of_day (float): The total distance traveled by the trucks by the end of the day.

    Returns:
        None

    Notes:
        time complexity:
            best case: O(n)
            worst case: O(n)
            average case: O(n)
        space complexity:
            best case: O(1)
            worst case: O(1)
            average case: O(1)
    """
    root = tkinter.PanedWindow(parent)  # O(n) - PanedWindow
    root.pack(fill="both", expand=1)  # O(n) - pack

    # Define attribute names as labels in the first row
    column_names = [
        "Total Distance Traveled at Time",
        "Total Distance Traveled by End of Day",
    ]

    for col, name in enumerate(column_names):  # O(n) - for loop
        label = tkinter.Label(root, text=name)
        label.grid(row=0, column=col)

    for i in range(len(column_names)):
        cell = tkinter.Label(
            root,
            text=total_distance_at_time if i == 0 else total_distance_by_end_of_day,
            borderwidth=1,
            relief="solid",
            bg="white",
        )
        cell.grid(row=1, column=i, sticky="nsew")
