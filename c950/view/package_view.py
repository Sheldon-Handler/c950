import csv

import c950
from c950.hash import csv_handler
from c950.model.package import Package
from c950 import defaults


def load_package_csv(csv_file: str) -> list:
    """
    Loads the package csv file.

    Returns:
        list: A list of all packages.
    """

    # Declare a list to store packages converted from sublist.
    package_list = []

    # Read the csv file and store it in a variable.
    csvhandler = csv_handler.read(csv_file)

    for row in csvhandler:
        package_list.append(Package(*row))

    c950.packages = package_list

    return package_list
