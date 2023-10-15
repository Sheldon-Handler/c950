"""
package.py file to store Package class.
:author: Sheldon Handler
"""


# Package class
class Package:
    """
    Package class to store package information.
    :class: Package
    :method: __init__: Constructor for Package class.
    :method: __str__: String representation of Package class.
    """

    # Constructor
    def __init__(self, package_id: int, address: str, city: str, state: str, zip_code: str, weight: int, deadline: str, note: str):
        """
        Constructor for Package class.
        :param: self: Package
        :type: self: Package
        :param: package_id: int
        :type: package_id: int
        :param: address: str
        :type: address: str
        :param: city: str
        :type: city: str
        :param: state: str
        :type: state: str
        :param: zip_code: str
        :type: zip_code: str
        :param: weight: int
        :type: weight: int
        :param: deadline: str
        :type: deadline: str
        :param: note: str
        :type: note: str
        """

        # Set package ID
        self.package_id = package_id

        # Set address
        self.address = address

        # Set city
        self.city = city

        # Set state
        self.state = state

        # Set zip code
        self.zip_code = zip_code

        # Set weight
        self.weight = weight

        # Set deadline
        self.deadline = deadline

        # Set note
        self.note = note

        # String representation
        def __str__(self):
            """
            String representation of Package class.
            :param: self: Package
            :type: self: Package
            :return: str
            """

            return f'Package ID: {self.package_id}, Address: {self.address}, City: {self.city}, State: {self.state}, Zip Code: {self.zip_code}, Weight: {self.weight}, Deadline: {self.deadline}, Note: {self.note}'
