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

from c950.model.truck import Truck
from __init__ import cursor


def get_all() -> list:
    """
    This function returns all trucks from the database.

    Returns:
        list: List of Truck objects.
    """

    cursor.row_factory = truck_row_factory

    query_result = cursor.execute(
        """
        SELECT *
        FROM truck
        """
    ).fetchall()

    return query_result


def get(id: int) -> Truck:
    query_result = cursor.execute(
        """
        SELECT *
        FROM truck
        WHERE id = ?
        """,
        (id),
    ).fetchone()

    return Truck(**query_result)


def set(truck: Truck) -> None:
    """
    This function sets a truck in the database.

    Args:
        truck (Truck): A Truck object.
    """

    cursor.execute(
        """
        UPDATE truck
        SET truck_status = ?,
        locations_assigned = ?,
        packages_assigned = ?,
        packages_loaded = ?,
        packages_delivered = ?
        """,
        (
            truck.truck_status,
            truck.locations_assigned,
            truck.packages_assigned,
            truck.packages_loaded,
            truck.packages_delivered,
        ),
    ).commit()


def truck_row_factory(cursor, row) -> Truck:
    """
    This function defines a row factory for the truck table.

    Args:
        cursor (): Cursor object to the database.
        row (): Row object from the database.

    Returns:
        Truck: Truck object from the database.
    """

    return Truck(**row)
