import unittest
import src


class TestPackage(unittest.TestCase):

    def test_package(self):
        package = src.c950.package.Package(1, "123 Main Street", "Salt Lake City", "UT", "84111", 10, "EOD", "Some note", src.c950.status.delivery_status.DeliveryStatus.AT_HUB)
        self.assertEqual(package.package_id, 1)
        self.assertEqual(package.address, "123 Main Street")
        self.assertEqual(package.city, "Salt Lake City")
        self.assertEqual(package.state, "UT")
        self.assertEqual(package.zip, "84111")
        self.assertEqual(package.weight_kilo, 10)
        self.assertEqual(package.delivery_deadline, "EOD")
        self.assertEqual(package.special_notes, "Some note")
        self.assertEqual(package.delivery_status, src.c950.status.delivery_status.DeliveryStatus.AT_HUB)


if __name__ == '__main__':
    unittest.main()