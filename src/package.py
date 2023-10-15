"""
package.py file to store Package class to store package information.
:import: dataclass from dataclasses
:class: Package
"""

# Import dataclass from dataclasses
from dataclasses import dataclass


@dataclass
class Package:
    """
    Package dataclass to store package information.
    :attributes: package_id, location, weight, deadline, note
    """

    # Package ID
    package_id: int

    # Address
    address: str

    # City
    city: str

    # State
    state: str

    # Zip code
    zip_code: str,

    # Weight
    weight: int

    #Deadline
    deadline: str

    # Note
    note: str


@dataclass
class Package:
    """
    Package class to store package information
    :attributes: package_id, address, city, state, zip_code, weight, deadline, note
    """

    # Package ID
    package_id: int

    # Address
    address: str

    # City
    city: str

    # State
    state: str

    # Zip code
    zip_code: str

    # Weight
    weight: int

    #Deadline
    deadline: str

    # Note
    note: str
