import struct

import package
from package import Package


class HashTable:
    """
    HashTable class to store key-value pairs
    """

    def __init__(self, size: int):
        """
        Initialize HashTable with size
        :param size: size of HashTable
        :type size: int
        """
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash(self, key: int):
        """
        Hash function to get index of key
        :param key: key to hash
        :type key: int
        :return: hash of key modulus size of table
        :rtype: int
        """
        return hash(key) % self.size

    def __getitem__(self, key):
        """
        Get item value from key
        :param key: key to get value from
        :return: item value from key if it exists, else raise KeyError
        :rtype: Package
        """
        index = self.hash(key)
        for item in self.table[index]:
            if item[0] == key:
                return item[1]
        raise KeyError(key)

    def __setitem__(self, key: int, value: Package):
        """
        Set item value from key
        :param key: key to set value from
        :type key: int
        :param value: value to set
        :type value: Package
        """
        index = self.hash(key)
        for item in self.table[index]:
            if item[0] == key:
                item[1] = value
                break
        self.table[index].append([key, value])

    def __delitem__(self, key: int):
        """
        Delete item from key
        :param key: key of item to delete
        :type key: int
        """
        index = self.hash(key)
        for item in self.table[index]:
            if item[0] == key:
                self.table[index].remove(item)
                break
            else:
                raise KeyError(key)

    def __iadd__(self, other):
        """
        Add item to HashTable
        :param other: item to add
        :type other: Package
        :return: self
        :rtype: HashTable
        """
        self[other.package_id] = other
        return self

    def __imod__(self, other):
        """
        Modify item in HashTable
        :param other: item to modify
        :type other: Package
        :return: self
        :rtype: HashTable
        """
        self[other.package_id] = other
        return self

    def __isub__(self, other):
        """
        Remove item from HashTable
        :param other: item to remove
        :type other: Package
        :return: self
        :rtype: HashTable
        """
        del self[other.package_id]
        return self
