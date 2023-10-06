"""
This file stores the template for object package
"""
from status import Status
from note import Note


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
                 deadline: str, note: Note, status: Status):
        """

        :param address: address for delivering package
        :param city: city for delivery of package
        :param state: state for delivery of package
        :param postal: postal code for delivery of package
        :param weight: weight of package
        :param deadline: deadline for delivery of package
        :param note: special note for package
        """
        setattr(__obj=self, __name="address", __value=address)
        setattr(__obj=self, __name="city", __value=city)
        setattr(__obj=self, __name="state", __value=state)
        setattr(__obj=self, __name="postal", __value=postal)
        setattr(__obj=self, __name="weight", __value=weight)
        setattr(__obj=self, __name="deadline", __value=deadline)
        setattr(__obj=self, __name="note", __value=note)
        setattr(__obj=self, __name="status", __value=status)


