import unittest

import src


class TestCsvHandler(unittest.TestCase):
    def test_write(self):
        csv_handler = src.c950.csv_handler.CsvHandler(filename="../resources/data/test.csv", header=["package_id", "address", "city", "state", "zip_code", "weight", "deadline", "note", "status"])

        csv_handler.write([[1, "123 Main Street", "Salt Lake City", "UT", "84111", 10, "EOD", "Some note", src.c950.status.package_status.PackageStatus.AT_HUB.name], [2, "123 Main Street", "Salt Lake City", "UT", "84111", 10, "EOD", "Some note", src.c950.status.delivery_status.DeliveryStatus.DELIVERED]])

        with open("../resources/data/test.csv", "r") as file:
            data = file.readlines()
            self.assertEqual(data[0], "package_id,address,city,state,zip_code,weight,deadline,note,status\n")
            self.assertEqual(data[1], "1,123 Main Street,Salt Lake City,UT,84111,10,EOD,Some note,AT_HUB\n")
            self.assertEqual(data[2], "2,123 Main Street,Salt Lake City,UT,84111,10,EOD,Some note,DELIVERED\n")

    def test_read(self):
        csv_handler = src.c950.csv_handler.CsvHandler("../resources/data/test.csv", header=["package_id", "address", "city", "state", "zip", "weight_kilo", "deadline", "note", "status"])

        self.assertEqual(csv_handler.read(), [["1", "123 Main Street", "Salt Lake City", "UT", "84111", "10", "EOD", "Some note", src.c950.status.delivery_status.DeliveryStatus.AT_HUB], ["2", "123 Main Street", "Salt Lake City", "UT", "84111", "10", "EOD", "Some note", src.c950.status.delivery_status.DeliveryStatus.DELIVERED.name]])


if __name__ == '__main__':
    unittest.main()
