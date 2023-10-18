"""hash_table.py.

This Python module defines a HashTable class with methods to add, modify, and delete key-value pairs.

Usage:
    Import this module and create instances of the HashTable class to work with key-value pairs.

Example:
    example_hash_table = HashTable(10)
    example_hash_table.insert("name", "Alice")
    custom_hash_table.get("name")  # Returns "Alice"
    custom_hash_table.delete("name")
"""

# Import Package from package
from package import Package, Status
# Import dataclass from dataclasses
from dataclasses import dataclass


# HashTable class
@dataclass
class HashTable:
    """HashTable class with methods to add, modify, and delete key-value pairs.

    Attributes:
        size (int): The size of the hash table.
        table (list): The underlying data structure to store key-value pairs.

    Methods:
        _hash_function(self, key): Hash function to calculate hash index.
        put(self, key, value): Set key-value pair to hash table.
        get(self, key): Get value from hash table.
        remove(self, key): Delete from hash table.
    """

    size: int = 10
    table: list = list

    def _hash_function(self, key):
        return hash(key) % self.size

    def get(self, key):
        index = self._hash_function(key)
        entry = self.table[index]
        if entry and entry[0] == key:
            return entry[1]
        else:
            return None

    def set(self, key, value):
        index = self._hash_function(key)
        self.table[index] = (key, value)

    def remove(self, key):
        """Remove a key-value pair from the hash table."""

        index = self._hash_function(key)
        entry = self.table[index]
        if entry and entry[0] == key:
            self.table[index] = None
        else:
            raise KeyError(f"Key '{key}' not found in the hash table")
