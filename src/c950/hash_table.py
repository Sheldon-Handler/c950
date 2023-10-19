"""This Python module defines a HashTable class with methods to add, modify,
and delete key-value pairs.

Usage:
    Import this module and create instances of the HashTable class to work with key-value pairs.

Example:
    example_hash_table = HashTable(10)
    example_hash_table.insert("name", "Alice")
    custom_hash_table.get("name")  # Returns "Alice"
    custom_hash_table.delete("name")
"""

# Import dataclass from dataclasses
from dataclasses import dataclass, field


# HashTable class
class HashTable:
    """HashTable to store key-value pairs.

    This hash table allows you to store key-value pairs and provides
    basic operations like insertion, retrieval, and deletion of items.

    Attributes:
        size (int): The size of the hash table.
        table (list): A list to store key-value pairs.

    Methods:
        hash(key): Computes the hash value for a given key.
        __getitem__(key): Retrieves the value associated with a given key.
        __setitem__(key, value): Inserts a key-value pair into the hash table.
        __delitem__(key): Removes a key-value pair from the hash table.
    """

    # Constructor
    def __init__(self, size: int):
        """Initialize the HashTable instance.

        Args:
            self (HashTable): The HashTable instance to initialize.
            size (int): The size of the hash table.

        Returns:
            HashTable: A HashTable instance with the specified size.

        References:
            https://docs.python.org/3/reference/datamodel.html#object.__init__
        """
        self.size = size
        self.table = [None] * size

    # Method to compute hash value for a given key
    def hash(self, key):
        """Compute the hash value for a given key.

        Args:
            key: The key for which the hash value is computed.

        Returns:
            int: The hash value for the key.
        """
        # Return sum of ASCII values of characters in key
        return sum(ord(char) for char in key) % self.size

    # Method to retrieve item from hash table
    def __getitem__(self, key):
        """Retrieve the value associated with a given key.

        Args:
            key: The key to search for.

        Returns:
            The value associated with the key, or None if the key is not found.
        """
        if self.table[self.hash(key)] is not None:
            for stored_key, value in self.table[self.hash(key)]:
                if stored_key == key:
                    return value
            raise IndexError(key)
        else:
            raise KeyError(key)

    # Method to set an item into hash table.
    def __setitem__(self, key, value):
        """Insert a key-value pair into the hash table.

        Args:
            key: The key for the item.
            value: The value associated with the key.
        """
        index = self.hash(key)
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            for i, (existing_key, existing_value) in enumerate(self.table[index]):
                if existing_key == key:
                    self.table[index][i] = (key, value)
                    break
            else:
                self.table[index].append((key, value))

    # Method to delete item from hash table
    def __delitem__(self, key):
        """Remove a key-value pair from the hash table.

        Args:
            key: The key to remove.
        """
        index = self.hash(key)
        if self.table[index] is not None:
            for i, (stored_key, _) in enumerate(self.table[index]):
                if stored_key == key:
                    del self.table[index][i]
                    break
