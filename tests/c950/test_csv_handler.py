import unittest

from src.c950.csv_handler import CsvHandler
from src.c950.status import Status


class TestCsvHandler(unittest.TestCase):
    def test_write(self):
        csv_handler = CsvHandler(filename="../resources/data/test.csv", header=["package_id", "address", "city", "state", "zip_code", "weight", "deadline", "note", "status"])

        csv_handler.write([[1, "123 Main Street", "Salt Lake City", "UT", "84111", 10, "EOD", "Some note", Status.PackageStatus.AT_HUB.name], [2, "123 Main Street", "Salt Lake City", "UT", "84111", 10, "EOD", "Some note", Status.PackageStatus.DELIVERED.name]])

        with open("../resources/data/test.csv", "r") as file:
            data = file.readlines()
            self.assertEqual(data[0], "package_id,address,city,state,zip_code,weight,deadline,note,status\n")
            self.assertEqual(data[1], "1,123 Main Street,Salt Lake City,UT,84111,10,EOD,Some note,AT_HUB\n")
            self.assertEqual(data[2], "2,123 Main Street,Salt Lake City,UT,84111,10,EOD,Some note,DELIVERED\n")

    def test_read(self):
        csv_handler = CsvHandler("../resources/data/test.csv", header=["package_id", "address", "city", "state", "zip_code", "weight", "deadline", "note", "status"])

        self.assertEqual(csv_handler.read(), [["1", "123 Main Street", "Salt Lake City", "UT", "84111", "10", "EOD", "Some note", Status.PackageStatus.AT_HUB.name], ["2", "123 Main Street", "Salt Lake City", "UT", "84111", "10", "EOD", "Some note", Status.PackageStatus.DELIVERED.name]])


if __name__ == '__main__':
    unittest.main()
