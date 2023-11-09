from c950.hash.hash_table import HashTable
from c950.controller.csv_handler import CsvHandler

package_hash_table = HashTable(10)  # Create a hash table with 40 buckets


class PackageDTO(HashTable):
    def __init__(self, size: int = 10):
        super().__init__(size)

    def __init_post__(self, package: Package):
        """
        Initializes a PackageDTO object. The package is added to the hash table.

        Args:
            package (Package): The package to add to the hash table.

        Returns:
            None
        """

        self.set(package.id, package)
