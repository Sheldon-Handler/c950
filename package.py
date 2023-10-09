"""
This file stores the template for object package
"""
import package
from status import Status


class Package:
    """
This class stores information about a package.
    """

    def __init__(self=package, address: str = "", city: str = "", state: str = "", postal: str = "", weight: int = None,
                 deadline: str = "", note: str = "", status: Status = Status.NOT_AVAILABLE):
        """

        :param address: address for delivering package
        :param city: city for delivery of package
        :param state: state for delivery of package
        :param postal: postal code for delivery of package
        :param weight: weight of package
        :param deadline: deadline for delivery of package
        :param note: special note for package
        """

        self.address = address
        self.city = city
        self.state = state
        self.postal = postal
        self.weight = weight
        self.deadline = deadline
        self.note = note
        self.status = status

    def __str__(self=package):
        return f"{self.address}, {self.city}, {self.state}, {self.postal}, {self.weight}, {self.deadline}, {self.note}, {self.status}"
