"""
This module contains the HashTable class. It is a custom hash table implementation with basic operations.
"""


class HashTable:
    """A custom hash table implementation.

    Args:
        size (int): The size of the hash table.

    Attributes:
        size (int): The size of the hash table.
        table (list): The hash table itself.
    """

    def __init__(self, size: int = 10):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key: int) -> int:
        """Returns an integer index for the given key.

        Args:
            key (Any): The key to hash.

        Returns:
            int: An integer index for the given key.
        """

        return key % self.size

    def add(self, key: int, value: object) -> None:
        """Adds a key-value pair to the hash table.

        Args:
            key (Any): The key to add.
            value (Any): The value to add.
        """

        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = []
        self.table[index].append((key, value))

    def get(self, key: int) -> Any:
        """Gets the value associated with the given key.

        Args:
            key (Any): The key to look up.

        Returns:
            Any: The value associated with the given key, or `None` if the key is not found.
        """

        index = self.hash_function(key)
        if self.table[index] is None:
            return None
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def remove(self, key: int) -> None:
        """Removes the key-value pair associated with the given key from the hash table.

        Args:
            key (Any): The key to remove.
        """

        index = self.hash_function(key)
        if self.table[index] is None:
            return
        for i in range(len(self.table[index])):
            if self.table[index][i][0] == key:
                del self.table[index][i]
                break

