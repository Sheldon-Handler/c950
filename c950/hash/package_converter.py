import datetime

from c950.model.truck import Truck
from c950.model.package import Package

from datetime import time


def convert_to_csv_list(package: Package):
    """Takes a Package object and converts it to a list of strings.

    Args:
        package (Package): Package to convert to a list for saving it in a csv file.

    Returns:

    """

    csv_list = [
        str(package.id),
        str(package.address),
        str(package.city),
        str(package.state),
        str(package.zip),
        str(package.delivery_deadline),
        str(package.weight_kilo),
        str(package.special_notes),
    ]
    return csv_list


def convert_to_package(package: list):
    """

    Args:
        package ():

    Returns:

    """

    new_package = Package(
        id = int(package[0]),
        address = str(package[1]),
        city = str(package[2]),
        state = str(package[3]),
        zip = str(package[4]),
        delivery_deadline = time(package[5]),
        weight_kilo = int(package[6]),
        special_notes = str(package[7]),
        delivery_status = (package[8]),
        truck_id = int(package[9]),
        delivery_time = str(package[10])
    )

    return new_package
