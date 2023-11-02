import dataclasses


@dataclasses.dataclass
class Address:
    """This dataclass represents an address instance with its information.

    Attributes:
        address (str): The address.
        city (str): The city.
        state (str): The state.
        zip (str): The zip code.

    Returns:
        Address: An Address class instance.
    """

    address: str
    city: str
    state: str
    zip: str
