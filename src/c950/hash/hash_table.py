"""
Module for the HashTable class.
"""


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# HashTable class
class HashTable:
    """
    A class for creating a hash table.

    Attributes:
        size: The size of the hash table.
        table: The hash table itself, implemented as an array of lists.
    """

    def __init__(self, size: int) -> None:
        """
        Initialize a new hash table with the given size.

        Args:
            size: The size of the hash table.
            table: The hash table itself, implemented as an array of lists.

        Returns:
            None
        """
        self.size = size
        self.table = [] * size

    def hash(self, item) -> int:
        """
        Return the hash value of the given key.

        Args:
            key: The key to hash.

        Returns:
            The hash value of the key.
        """

        return item.__hash__() % self.size

    # Method to get the value associated with the given key.
    def __getitem__(self, key: int) -> object:
        """
        Get the value associated with the given key.

        Args:
            key: The key to look up.

        Returns:
            The value associated with the key, or None if the key is not found.
        """
        index = self.hash(key)
        key_value_pair = self.table[index]
        if key_value_pair is None:
            return None
        else:
            return key_value_pair

    def __setitem__(self, key: int, value: object) -> None:
        """
        Add a new key-value pair to the hash table.

        Args:
            key: The key to add.
            value: The value to add.

        Returns:
            None
        """
        index = self.hash(key)
        self.table[index] = (key, value)

    def __delitem__(self, key: int) -> None:
        """
        Remove the key-value pair associated with the given key from the hash table.

        Args:
            key: The key to remove.
        """

        index = self.hash(key)
        if self.table[index] is None:
            return
        for i in self.table[index]:
            if self.table[index][i][0] == key:
                del self.table[index][i]
                break
