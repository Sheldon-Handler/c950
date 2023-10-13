"""
package.py file to store Package class to store package information.
:imports status: Status class to store status of package delivery.
:classes Package: Package class to store package information
"""
from status import Status


class Location:
    """
    Location class to store location information
    :attributes: address, city, state, postal
    :methods: __init__, __str__
    """

    # Address
    address: str

    # City
    city: str

    # State
    state: str

    # Postal
    postal: str

    # Constructor
    def __init__(self, address: str, city: str, state: str, postal: str):
        """
        Initialize location with address, city, state, and postal.
        :param self: location to initialize
        :type self: Location
        :param address: address for delivering package
        :type address: str
        :param city: city for delivery of package
        :type city: str
        :param state: state for delivery of package
        :type state: str
        :param postal: postal code for delivery of package
        :type postal: str
        :methods: __init__, __str__
        """

        self.address = address
        self.city = city
        self.state = state
        self.postal = postal

    def __str__(self):
        """
        String representation of location
        :param self: location to get string representation of
        :type self: Location
        :return: string representation of location
        :rtype: str
        """

        # Return string representation of location
        return f"{self.address}\n" \
               f"{self.city}, {self.state} {self.postal}\n"

class Details:
    """
    Details class to store delivery details
    :attributes: deadline, note, status
    :methods: __init__, __str__
    """

    # Weight
    weight: int

    # Deadline
    deadline: str

    # Note
    note: str

    # Constructor
    def __init__(self, weight: int, deadline: str, note: str):
        """
        Initialize delivery_details with deadline, note, and status.
        :param self: delivery_details to initialize
        :type self: delivery_details
        :param deadline: deadline for delivery of package
        :type deadline: str
        :param note: special note for package
        :type note: str
        """

        self.weight = weight
        self.deadline = deadline
        self.note = note

    def __str__(self):
        """
        String representation of delivery_details
        :param self: delivery_details to get string representation of
        :type self: delivery_details
        :return: string representation of delivery_details
        :rtype: str
        """

        # Return string representation of delivery_details
        return f"Weight: {self.weight}\n" \
               f"Deadline: {self.deadline}\n" \
               f"Note: {self.note}\n"


class Package:
    """
    Package class to store package information
    :attributes: package_id, location, weight, deadline, note, status
    :methods: __init__, __str__
    """

    # Package ID
    package_id: int

    # Location
    location: Location

    # Details
    details: Details

    # Constructor
    def __init__(self, package_id: int, location: Location, details: Details, status: Status):
        """
        Initialize package with package_id, location, weight, deadline, note, and status.
        :param self: package to initialize
        :type self: Package
        :param package_id: id of package
        :type package_id: int
        :param location: location of package
        :type location: Location
        :param details: details of package
        :type details: Details
        :param status: status of package
        :type status: Status
        :methods: __init__, __str__
        """

        self.package_id = package_id
        self.location = location
        self.details = details
        self.status = status

    # Method to get string representation of package
    def __str__(self):
        """
        String representation of package
        :param self: package to get string representation of
        :type self: Package
        :return: string representation of package
        :rtype: str
        """

        # Return string representation of package
        return f"Package ID: {self.package_id}\n" \
               f"Location: {self.location}\n" \
               f"Weight: {self.weight}\n" \
               f"Status: {self.status.name}\n"
