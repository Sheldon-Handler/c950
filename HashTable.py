import datetime
import enum

hash_table = []


class DeliveryStatus(enum.Enum):
    NOT_AVAILABLE = 0
    AT_THE_HUB = 1
    EN_ROUTE = 2
    DELIVERED = 3


# Class for storing the details of each delivery_package
class DeliveryPackage:

    def __init__(self, address: str, deadline: datetime.time,
                 city: str, postal: str, weight: float, status: DeliveryStatus):
        """

        :param address: address for delivering package
        :param deadline: deadline for delivery of package
        :param city: city for delivery of package
        :param postal: postal code for delivery of package
        :param weight: weight of package
        :param status: delivery status of package
        """
        self.address = address
        self.deadline = deadline
        self.city = city
        self.postal = postal
        self.weight = weight
        self.status = status


class HashTable:
    def __add__(self, delivery_package: DeliveryPackage):
        hash_table.append(__object=delivery_package)

    def __setitem__(self, key: int, value: DeliveryPackage):
        hash_table.__setitem__(__i=key, __o=value)

    def __delitem__(self, item):
        if isinstance(__obj=item, __class_or_tuple=int):
            hash_table.__delitem__(item)
        elif isinstance(__obj=item, __class_or_tuple=DeliveryPackage):
            hash_table.remove(__value=item)
