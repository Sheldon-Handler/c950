from enum import Enum


# enum class for the delivery status of the package
class Status(Enum):
    NOT_AVAILABLE = 0
    AT_THE_HUB = 1
    EN_ROUTE = 2
    DELIVERED = 3
