"""This module contains the PackageDAO class to store Package class in
"package" table of "identifier.sqlite" database."""

#  MIT License
#
#  Copyright (c) <year> <copyright holders>
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice (including the next paragraph) shall be included in all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import sqlite3

from c950.model.package import Package
import sqlite3.dbapi2
from __init__ import cursor


def get_package(package_id: int) -> Package:
    """Returns a Package from the 'package' table in 'identifier.sqlite'.
    Raises an exception if there is an error.

    Args:
        package_id (int): The package_id of the Package to return.

    Returns:
        Package: The Package with the specified package_id.
    """

    try:
        return (
            cursor()
            .execute("SELECT * FROM package WHERE package_id = ?", package_id)
            .fetchone()
        )
    except sqlite3.Error as e:
        raise e


def get_packages() -> list:
    """Returns all packages from the 'package' table in
    'identifier.sqlite'. Raises an exception if there is an error.

    Returns:
        list: A list of all packages from the 'package' table in
            'identifier.sqlite'.
    """

    try:
        return cursor().execute("SELECT * FROM package").fetchall()
    except sqlite3.Error as e:
        raise e


def add_package(package: Package):
    """Adds a Package to the package table in packages.db.

    Args:
        package (Package): The package to add.
    """

    if not isinstance(package, Package):
        raise TypeError("package must be a Package object.")
    else:
        try:
            cursor.execute(
                "INSERT INTO package VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (
                    package.id,
                    package.address,
                    package.city,
                    package.state,
                    package.zip,
                    package.delivery_deadline,
                    package.weight_kilo,
                    package.special_notes,
                    package.delivery_status.value,
                    package.truck,
                    package.delivery_time,
                ),
            )
            cursor.commit()
        except sqlite3.Error as e:
            raise e


def add_packages(list_of_packages: list):
    """Inserts a list of packages into the package table in packages.db.

    Args:
        list_of_packages (list): A list of packages to insert.
    """

    # Check if all elements in list_of_packages are Package objects.
    if not all(isinstance(package, Package) for package in list_of_packages):
        raise TypeError("list_of_packages must only contain Package objects.")
    else:
        try:
            cursor.executemany(
                "INSERT INTO package VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                list_of_packages,
            )
            cursor.commit()
        except sqlite3.Error as e:
            raise e


def remove_package(package: Package or int):
    """Removes a Package from the "package" table in the
    "identifier.sqlite" database.

    Args:
        package (int or Package): The package to remove.

    Returns:
        None
    """

    if isinstance(package, Package):
        cursor.execute("DELETE FROM package WHERE package_id = ?", package.id).commit()
    elif isinstance(package, int):
        cursor.execute("DELETE FROM package WHERE package_id = ?", package).commit()
    else:
        raise TypeError("package must be an int or Package object.")


def remove_packages(packages: list):
    """Removes a list of Packages from the "package" table in the
    "identifier.sqlite" database.

    Args:
        packages (list): The list of packages to remove.

    Returns:
        None
    """

    # Check if all elements in packages are Package objects or int Package id's.
    if not all(isinstance(package, Package or int) for package in packages):
        raise TypeError(
            "package must be a list of Package objects and/or int Package id's."
        )

    # Set all Package objects to their id's.
    for i in range(len(packages)):
        if isinstance(packages[i], Package):
            packages[i] = packages[i].id

    cursor.executemany("DELETE FROM package WHERE package_id = ?", packages).commit()


def update_package(package: Package):
    """Updates a Package in the package table.

    Args:
        package (Package): The Package object to update.

    Returns:
        None
    """
    if not isinstance(package, Package):
        raise TypeError("package must be a Package object.")

    try:
        cursor.execute(
            """
            UPDATE package
            SET address = ?,
                city = ?,
                state = ?,
                zip = ?,
                delivery_deadline = ?,
                weight_kilo = ?,
                special_notes = ?,
                status = ?,
                truck = ?,
                delivery_time = ?
            WHERE package_id = ?;
            """,
            (
                package.address,
                package.city,
                package.state,
                package.zip,
                package.delivery_deadline,
                package.weight_kilo,
                package.special_notes,
                package.delivery_status,
                package.truck.id,
                package.delivery_time,
                package.id,
            ),
        )
        cursor.commit()
    except sqlite3.Error as e:
        raise e
