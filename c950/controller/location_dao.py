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


def get_locations() -> list:
    cursor.row_factory = location_row_factory

    query_result = cursor.execute(
        """
        SELECT *
        FROM location
        """
    ).fetchall()

    return query_result


def get_location(id: int) -> Location:
    cursor.row_factory = location_row_factory

    location = cursor.execute(
        """
        SELECT *
        FROM location
        WHERE id = ?
        """,
        id,
    ).fetchall()

    return location


def filter_locations(
    id: int = None,
    name: str = None,
    address: str = None,
    city: str = None,
    state: str = None,
    zip: str = None,
):
    cursor.row_factory = location_row_factory

    query = "SELECT * FROM location WHERE "
    conditions = []
    values = []

    attributes = locals()

    previous_condition_appended = False

    for key, value in attributes.keys(), attributes.values():
        if value is not None:
            if previous_condition_appended is True:
                query += " AND "
            query += key + " = ?"

            conditions.append(key)
            values.append(value)
            previous_condition_appended = True

    result = cursor.execute(query, values).fetchall()

    return result


def filter_locations_by_params(location, search_params):
    return all(
        getattr(location, key, None) == value for key, value in search_params.items()
    )


def search_locations(search_params):
    locations = get_locations()

    for locations in locations:
        if filter_locations_by_params(locations, search_params):
            return locations


def search_location_matches(id, name, address, city, state, zip):
    list_of_locations = get_locations()

    matching_locations = []

    for location in list_of_locations:
        if match_location(location, id, name, address, city, state, zip) is True:
            matching_locations.append(location)


def match_location(
    location: Location = None,
    id: int = None,
    name: str = None,
    address: str = None,
    city: str = None,
    state: str = None,
    zip: str = None,
) -> bool:
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


def find_matching_locations(locations, search_params):
    filtered_locations = filter(
        lambda x: filter_locations_by_params(x, search_params), locations
    )
    return list(filtered_locations)


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
        locations.append(location_converter(l))

    return locations


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
    Takes a Location list and returns it as a Location object.

    Args:
        location (Location): A Location as a list.

    Returns:
        Location: Location as a Location object
    """

    return Location(*location)


def location_row_factory(cursor, row):
    location = Location(*row)
    return location
