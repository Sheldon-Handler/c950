import sqlite3
from __init__ import cursor


def get_all():
    cursor.execute(
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
