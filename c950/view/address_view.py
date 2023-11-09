import types

from c950.hash.hash_table import HashTable
from c950.model.package import Package
from c950.hash.csv_handler import CsvHandler
from c950.__init__ import *

package_hash_table = HashTable(10)  # Create a hash table with 40 buckets


class PackageDTO(HashTable, CsvHandler):
    def __init__(self, filename: str = package_csv_file, size: int = 10):
        super().__init__(size)
        super().__init__(filename, Package)

    def add_package(self, package):
        self.set(package.package_id, package)

    def get_package(self, package_id):
        return self.get(package_id)

    def get_packages(self):
        return self.table

    def update_package(self, package):
        self.set(package.package_id, package)

    def remove_package(self, package_id):
        self.remove(package_id)
