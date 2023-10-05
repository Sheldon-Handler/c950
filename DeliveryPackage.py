# This class stores the information for each delivery package.
import enum


delivery_status = ["not_available", "at_the_hub", "en_route", "delivered"]


# Class for storing the details of each delivery_package
def delivery_package(package_id: int, address: str, deadline: (int, int), city: str, postal: str, weight: float,
                     status: delivery_status):
    """

    :param package_id: id of package
    :param address: address for delivering package
    :param deadline: deadline for delivery of package
    :param city: city for delivery of package
    :param postal: postal code for delivery of package
    :param weight: weight of package
    :param status: delivery status of package
    """
    package_id = package_id
    address = address
    deadline = deadline
    city = city
    postal = postal
    weight = weight
    status = status
