# This class stores the information of a delivery package.

from status import Status


class Package:
    address: str
    city: str
    state: str
    zip: str
    country: str
    weight: int
    deadline: str
    note: str

    def __init__(self, address: str, city: str, state: str, zip: str, weight: int,
                 deadline: str, note: str):
        """

        :param address: address for delivering package
        :param city: city for delivery of package
        :param state: state for delivery of package
        :param zip: zip code for delivery of package
        :param weight: weight of package
        :param deadline: deadline for delivery of package
        :param note: special note for package
        """
        address = address
        city = city
        state = state
        zip = zip
        weight = weight
        deadline = deadline
        note = note


# Class for storing the details of each delivery_package
class DeliveryPackage(Package):

    status: Status


    def __init__(self, status, address, city, state, zip, deadline, weight, note):
        super().__init__(address=address, city=city, state=state, zip=zip,
                         deadline=deadline, weight=weight, note=note)

    """

        :param address: address for delivering package
        :param city: city for delivery of package
        :param state: state for delivery of package
        :param zip: zip code for delivery of package
        :param weight: weight of package
        :param deadline: deadline for delivery of package
        :param note: special note for package
        :param status: delivery status of package
        """

