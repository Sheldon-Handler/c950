"""
This file stores the template for object package
"""
import this

from status import Status


class Package:
    """
This class stores information about a package.
    """
    address: str
    city: str
    state: str
    postal: str
    country: str
    weight: int
    deadline: str
    note: str

    def __init__(self, address: str, city: str, state: str, postal: str, weight: int,
                 deadline: str, note: str, status: Status):
        """

        :param address: address for delivering package
        :param city: city for delivery of package
        :param state: state for delivery of package
        :param postal: postal code for delivery of package
        :param weight: weight of package
        :param deadline: deadline for delivery of package
        :param note: special note for package
        """

        super.address = address
        city = city
        state = state
        postal = postal
        weight = weight
        deadline = deadline
        Package.note = note
        Package.status = status
