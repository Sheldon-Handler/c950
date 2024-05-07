import dataclasses


@dataclasses.dataclass(frozen=True, order=True)
class Address:
    """This dataclass represents an address instance with its information.

    Attributes:
        id (int): The id of the location.
        name (str): The name of the location.
        address (str): The address.

    Returns:
        Address: An Address object instance.
    """

    id: int
    name: str
    address: str
