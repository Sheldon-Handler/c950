
from enum import Enum
from dataclasses import dataclass
from package import Package
from truck import Truck
import time


class DeliveryStatus(Enum):
    """This enum represents the delivery status of a package.

    Attributes:
        NOT_AVAILABLE (int): The package is not available.
        AT_HUB (int): The package is at the hub.
        EN_ROUTE (int): The package is en route.
        DELIVERED (int): The package has been delivered.

    Returns:
        DeliveryStatus: A DeliveryStatus enum instance.
    """

    NOT_AVAILABLE = 0
    AT_HUB = 1
    EN_ROUTE = 2
    DELIVERED = 3


@dataclass
class PackageStatus(Package):
    """This dataclass represents a package status instance with its information.

    Attributes:
        delivery_status (DeliveryStatus): The package delivery status.
        truck (Truck): The package delivery truck.
        loaded_time (time): The package loaded time.
        delivery_time (time): The package delivery time.

    Returns:
        PackageStatus: A PackageStatus class instance.
    """

    delivery_status: DeliveryStatus
    truck: Truck
    loaded_time: time
    delivery_time: time
