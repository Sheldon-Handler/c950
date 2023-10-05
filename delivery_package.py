# This class stores the information of a delivery package.
import datetime
import status


# Class for storing the details of each delivery_package
class DeliveryPackage:
    def __init__(self, address: str, deadline: datetime.time, city: str, postal: str, weight: float, status: status.Status):
        """

        :param address: address for delivering package
        :param deadline: deadline for delivery of package
        :param city: city for delivery of package
        :param postal: postal code for delivery of package
        :param weight: weight of package
        :param status: delivery status of package
        """
        address = address
        deadline = deadline
        city = city
        postal = postal
        weight = weight
        status = status
