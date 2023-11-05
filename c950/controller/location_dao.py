import sqlite3
from __init__ import cursor
from c950.model.location import Location


def get_locations():
    query_result = cursor.execute(
        """
        SELECT UNIQUE
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
        SELECT
        (   
            id,
            address,
            city,
            state,
            zip
        )
            FROM package
            WHERE zip = ?
            """,
        zip
    ).fetchall()

    return _to_list_of_locations(location_list)


def _to_list_of_locations(location_list: list) -> list:
    """
    Takes a location list where each location attribute is a sublist
    and returns a list of Location objects.

    Args:
        location_list (list): List of location details.

    Returns:

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
        location_detail_list[3]
    )
