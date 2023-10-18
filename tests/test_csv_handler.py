import unittest

from c950.csv_handler import CsvHandler
import pkgutil
import pathlib

class MyTestCase(unittest.TestCase):
    def test_something(self):
        csv_handler = CsvHandler("data.csv", header=["package_id", "address", "city", "state", "zip_code", "weight", "deadline", "note", "status"])


        self.assertEqual(True, False)  # add assertion here

    def test_read(self):
        csv_handler = CsvHandler(pathlib.Pa, header=["package_id", "address", "city", "state", "zip_code", "weight", "deadline", "note", "status"])
        data = csv_handler.read()
        for row in data:
            print(row)



if __name__ == '__main__':
    unittest.main()
