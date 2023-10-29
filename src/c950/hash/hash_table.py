"""This module contains the HashTable class.
"""
#  MIT License
#
#  Copyright (c) 2023 Sheldon Handler
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice (including the next paragraph) shall be included in all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import bisect


class HashTable:
    """
    A hash table implementation that uses chaining to prevent hash collisions.

    Args:
        size (int): The size of the hash table.

    Attributes:
        table (list): The hash table.

    Methods:
        hash: Hashes the given key to a hash value.
        set: Sets the value for the given key in the hash table.
        get: Gets the value for the given key in the hash table.
        remove: Removes the key-value pair for the given key from the hash table.
        __str__: Returns a string representation of the hash table.

    Returns:
        HashTable: A HashTable class instance.

    Examples:
        >>> table = HashTable()
        >>> table.set(1, 'Example Value 1')
        >>> table.set(2, 'Example Value 2')
        >>> table.set(3, 'Example Value 3')
        >>> print(table.get(1))
        Example Value 1
        >>> print(table.get(2))
        Example Value 2
        >>> print(table.get(3))
        Example Value 3
        >>> table.remove(2)
        >>> print(table.get(2))
        None
        >>> print(table)
        1:Example Value 1
        3:Example Value 3
    """

    def __init__(self, size: int = 10) -> None:
        """
        Initializes a HashTable object.

        Args:
            size (int): The initial size of the hash table parent list. Defaults to 10.

        Returns:
            None
        """

        self.table = []
        for i in range(size):
            self.table.append([])

    def hash(self, key) -> int:
        """
        Hashes the given key to a hash value.

        Args:
            key: The key to hash.

        Returns:
            int: The hash value.
        """

        return hash(key) % len(self.table)

    def set(self, key, value) -> None:
        """
        Sets the value for the given key in the hash table.

        Args:
            key: The key to set the value for.
            value: The value to set.

        Returns:
            None
        """
        # Get the index of the bucket for the key
        bucket = self.hash(key)
        # Check if the key already exists in the hash table
        for i, (k, v) in enumerate(self.table[bucket]):
            # If the key already exists, replace the value
            if k == key:
                # Replace the value
                self.table[bucket][i] = (key, value)
                # Exit the function
                return
        # Otherwise, append the key-value pair to the bucket
        self.table[bucket].append((key, value))
        # Then, sort the bucket in ascending order
        self.table[bucket].sort()

    def get(self, key) -> any:
        """
        Gets the value for the given key in the hash table.

        Args:
            key: The key to get the value for.

        Returns:
            any: The value for the given key, or None if the key does not exist.
        """
        # Get the index of the bucket for the key
        bucket = self.hash(key)
        # Iterate through the bucket to find the key
        for k, v in self.table[bucket]:
            # If the key exists, return the value
            if k == key:
                # Return the value
                return v
        # Otherwise, return None
        return None

    def remove(self, key) -> None:
        """
        Removes the key-value pair for the given key from the hash table.

        Args:
            key: The key to remove the key-value pair for.

        Returns:
            None
        """

        bucket = self.hash(key)  # Index of the bucket containing the key-value pair

        item_to_delete = self.__binary_search__(key)  # Find the index of the key in the bucket

        if item_to_delete is not None:  # If the key is found in the bucket
            self.table[bucket].pop(item_to_delete)  # Remove the key-value pair from the bucket

    def __binary_search__(self, key):
        """
        Perform a binary search on a sorted array to find the target element.

        Args:
            key: The key to find in the hash table.

        Returns:
            int: The index of the target element in the array, or None if the element is not found.
        """
        bucket = self.hash(key)  # Index of the bucket containing the key-value pair

        low = 0  # The low pointer in the search range. Initially, this is the first index.

        high = len(self.table[bucket]) - 1  # The high pointer in the search range. Initially, this is the last index.

        while low <= high:  # Iterate through the bucket to find the key
            mid = (low + high) // 2  # Calculate the middle index between the previous search range

            if self.table[bucket][mid] < key:
                low = mid + 1  # Adjust the 'low' pointer
            elif self.table[bucket][mid] > key:
                high = mid - 1  # Adjust the 'high' pointer
            else:  # If the key is found
                return mid  # Return the index of the key

        return None  # If the element was not found in the array. Return None.

    def __str__(self) -> str:
        """
        Returns a string representation of the hash table.

        Returns:
            str: A string representation of the hash table.
        """

        table_size = len(self.table)
        string = ''
        for i in range(table_size):
            for k, v in self.table[i]:
                string += str(k) + ':' + str(v) + '\n'

        return string


if __name__ == '__main__':
    table = HashTable(96)

    table.set(1, 'a')
    table.set(13, 'b')
    table.set(3, 'c')
    table.set(18, 't')
    table.set(12, 'tc')
    table.set(35, 'tm')
    table.set(9, 'bq')
    table.set(7, 'pr')
    table.set(2, 'db')
    table.set(4, 'testr')
    table.set(5, 'test')
    table.set(6, 'ltest')

    print(table.get(1))
    print(table.get(12))
    print(table.get(24))

    table.remove(12)

    print(table.get(2))

    print(table)
