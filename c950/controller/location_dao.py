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

from c950.model.location import Location
from __init__ import cursor
import sqlite3


def set(location: Location) -> None:
    """
    This function sets a location in the database.

    Args:
        location (Location): A Location object.
    """

    try:
        cursor.execute(
            """
            INSERT INTO location
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                location.id,
                location.name,
                location.address,
                location.city,
                location.state,
                location.zip,
            ),
        )
        cursor.commit()
    except sqlite3.Error as e:
        raise e


def get_all() -> list:
    cursor.row_factory = location_row_factory

    query_result = cursor.execute(
        """
        SELECT *
        FROM location
        """
    ).fetchall()

    return query_result


def search_location_matches(
    id: int = None,
    name: str = None,
    address: str = None,
    city: str = None,
    state: str = None,
    zip: str = None,
) -> list:
    """
    Searches for locations that match the given parameters.

    Args:
        id (int): The location id.
        name (str): The location name.
        address (str): The location address.
        city (str): The location city.
        state (str): The location state.
        zip (str): The location zip code.

    Returns:
        list: A list of locations that match the given parameters.
    """
    list_of_locations = get_all()

    matching_locations = []

    for location in list_of_locations:
        if match_location(location, id, name, address, city, state, zip) is True:
            matching_locations.append(location)

    return matching_locations


def match_location(
    location: Location = None,
    id: int = None,
    name: str = None,
    address: str = None,
    city: str = None,
    state: str = None,
    zip: str = None,
) -> bool:
    """Checks if a location matches the given parameters. If a parameter is None, than anything will match it.

    Args:
        location (Location): A location object.
        id (int): The location id.
        name (str): The location name.
        address (str): The location address.
        city (str): The location city.
        state (str): The location state.
        zip (str): The location zip.

    Returns:
        bool: True if the location matches the parameters, else False.
    """

    if location.__class__ is not Location:
        raise ValueError("Please provide a location.")
    elif (
        (id == location.id or id is None)
        and (name == location.name or name is None)
        and (address == location.address or address is None)
        and (city == location.city or city is None)
        and (state == location.state or state is None)
        and (zip == location.zip or zip is None)
    ):
        return True
    else:
        return False


def location_row_factory(cursor, row):
    location = Location(*row)
    return location
