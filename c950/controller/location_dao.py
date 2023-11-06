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

from __init__ import cursor
from c950.model.location import Location


def get_locations():
    query_result = cursor.execute(
        """
        SELECT DISTINCT
        (
            address,
            city,
            state,
            zip
        )
            FROM package
            """
    ).fetchall()

    return _to_list_of_locations(query_result)


def get_location_by_zip(zip: str) -> list:
    location_list = cursor.execute(
        """
        SELECT DISTINCT
        (   
            address,
            city,
            state,
            zip
        )
            FROM package
            WHERE zip = ?
            """,
        zip,
    ).fetchall()

    return _to_list_of_locations(location_list)


def find_matching_locations(location: Location) -> Location:
    """
    Finds locations that match the given location.

    Returns:
        Location: A Location object with the matching location details.
    """
    for item in get_locations():
        if (
            item.address == location.address
            and item.city == location.city
            and item.state == location.state
            and item.zip == location.zip
        ):
            return item.id

    return None


def find_matching_address_and_zip(location: Location) -> Location:
    for item in get_locations():
        if item.address == location.address and item.zip == location.zip:
            return item.id


def _to_list_of_locations(location_list: list) -> list:
    """
    Takes a location list where each location attribute is a sublist
    and returns a list of Location objects.

    Args:
        location_list (list): List of location details.

    Returns:
        list: List of Location objects.
    """
    locations = []

    for l in location_list:
        locations.append(__to_location_object__(l))

    return locations


def __to_location_object__(location_detail_list: list) -> Location:
    """
    Takes a list of location details and returns the location as a Location object.

    Args:
        location_detail_list (list): List of location details.

    Returns:
        Location: Location object with the location details.
    """

    return Location(
        location_detail_list[0],
        location_detail_list[1],
        location_detail_list[2],
        location_detail_list[3],
    )


def location_adapter(location: Location) -> tuple:
    """
    Takes a Location object and returns a tuple of the location details.

    Args:
        location (Location): A Location object.

    Returns:
        tuple: A tuple of the location details.
    """

    return (location.address, location.city, location.state, location.zip)


def location_converter(location: list) -> Location:
    """
    Takes a Location object and returns a tuple of the location details.

    Args:
        location (Location): A Location object.

    Returns:
        list: Location as a Location object
    """

    return Location(*location)
