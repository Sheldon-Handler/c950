import csv

from c950.hash.csv_handler import CsvHandler
from c950.controller import json_handler
from c950 import package_csv_file
from c950.model.package import Package


class PackageView:
    """
    This class is a view for the package csv file.

    Attributes:
        csv_handler (CsvHandler): A CsvHandler instance.
    """

    def __init__(self, csv_file: str, json_file: str):
        """
        Initializes the PackageView class.
        """
        self.csv_file = csv_file
        self.json_file = json_file

    def read(self):
        """
        Gets all packages from the csv file.

        Returns:
            list: A list of all packages.
        """

        # Declare a list to store packages converted from sublist.
        package_list = []

        #
        csvhandler = CsvHandler(self.csv_file)
        package_csv_reader = csvhandler.read()
        for row in package_csv_reader:
            package_list.append(Package(*row))


    def set(self):
        """
        Sets the csv file with the updated packages.

        """
        self.csv_handler.set()
