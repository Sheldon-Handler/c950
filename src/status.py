from enum import Enum


class Status(Enum):
    """
    Status enum to store package status
    :param Enum: enum to inherit from
    :type Enum: Enum

    """

    NOT_AVAILABLE = 0
    AT_THE_HUB = 1
    EN_ROUTE = 2
    DELIVERED = 3
