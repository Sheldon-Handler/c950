"""
This file stores the template for object package
"""


class Package:

    """
This class stores information about a package.
    """

    def __init__(self, package_id: int, address: str, city: str, state: str, postal: str, weight: int, deadline: str,
                 note: str, status: "str"):
        """

        :param package_id: id of package
        :param address: address for delivering package
        :param city: city for delivery of package
        :param state: state for delivery of package
        :param postal: postal code for delivery of package
        :param weight: weight of package
        :param deadline: deadline for delivery of package
        :param note: special note for package
        :param status: status of package delivery
        """

        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.postal = postal
        self.weight = weight
        self.deadline = deadline
        self.note = note
        self.status = status

    def __hash__(self):
        return hash(self.package_id)

    def update_status(self, new_status):
        self.status = new_status

    def __str__(self):
        return f"Delivery Package - Address: {self.address}, City: {self.city}, State: {self.state}, Postal: {self.postal}, Weight: {self.weight}, Deadline: {self.deadline}, Note: {self.note}, Status: {self.status}"


