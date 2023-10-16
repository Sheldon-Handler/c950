"""
package.py file to store Package class.
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
        :param: self: self reference
        :type: self: Package
        :param: package_id: id of package
        :type: package_id: int
        :param: address: address of package
        :type: address: str
        :param: city: city of package
        :type: city: str
        :param: state: state of package
        :type: state: str
        :param: zip_code: zip code of package
        :type: zip_code: str
        :param: weight: weight of package
        :type: weight: int
        :param: deadline: deadline of package
        :type: deadline: str
        :param: note: note of package
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
