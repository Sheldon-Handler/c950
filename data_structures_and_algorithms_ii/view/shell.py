import argparse
import data_structures_and_algorithms_ii


class Shell:
    """
    This class is the command line interface for the package delivery service.

    Attributes:
        parser (ArgumentParser): The argument parser for the command line interface.

    Returns:
        Shell: A Shell class instance.

    Notes:
        time complexity: O(1)
        space complexity: O(1)
    """

    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Package Delivery Service")
        self.parser.add_argument(
            "-d",
            "--debug",
            help="Show debug information",
            action="store_true",
            required=False,
        )

        self.parser.add_argument(
            "-",
            "--",
            help="Run unit tests",
            action="store_true",
            required=False,
        )

    def correct_address(self, package_id, correct_address) -> None:
        """
        Updates the address of a package.

        Args:
            package_id (int): The id of the package to update.
            correct_address (str): The correct address for the package.

        Notes:
            time complexity: O(n)
            space complexity: O(1)
        """
        # Get the package by its id, then modify its address
        data_structures_and_algorithms_ii.model.package.get_package_by_id(
            package_id
        ).address = correct_address
