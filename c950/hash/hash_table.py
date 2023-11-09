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
        __binary_search__: Perform a binary search on the hash table to find the specified element.
        __str__: Returns a string representation of the hash table.

    Returns:
        HashTable: A HashTable class instance.
    """

    def __init__(self, size: int = 10) -> None:
        """
        Initializes a HashTable object. The hash table is initialized as a list of buckets. Each bucket is a list of
        key-value pairs.

        Args:
            size (int): The initial size of the hash table parent list. Defaults to 10.

        Returns:
            None
        """

        self.table = []  # Initialize the hash table as an empty list
        for i in range(
            size
        ):  # For each index in the range of the size of the hash table
            self.table.append(
                []
            )  # Append an empty list to the hash table to create a bucket

    def hash(self, key) -> int:
        """
        Hashes the given key to a hash value.

        Args:
            key: The key to hash.

        Returns:
            int: The hash value.
        """

        return hash(key) % len(self.table)  # Hash the key and return the hash value

    def set(self, key, value) -> None:
        """
        Sets the value for the given key in the hash table.

        Args:
            key: The key to set the value for.
            value: The value to set.

        Returns:
            None
        """
        bucket = self.hash(key)  # Get the index of the bucket for the key-value pair
        for i, (k, v) in enumerate(
            self.table[bucket]
        ):  # Check if the key exists in the bucket
            if k == key:  # If the key exists in the bucket
                self.table[bucket][i] = value  # Replace the value at the key index
                return  # Exit the function
        self.table[bucket].append(
            (key, value)
        )  # Append the key-value pair to the bucket if the key does not exist
        self.table[bucket].sort()  # Sort the bucket by key in ascending order

    def set_all(self, keys: list, items: list) -> None:
        """
        Sets the value for the given key in the hash table.
        Args:
            keys (list): The keys to set the values for.
            items (list): The values to set.

        Returns:
            None
        """
        for i in range(len(keys)):  # Iterate through each key-value pair
            self.set(keys[i], items[i])  # Set the key-value pair in the hash table

    def get(self, key) -> any:
        """
        Gets the value for the given key in the hash table.

        Args:
            key: The key to get the value for.

        Returns:
            any: The value for the given key, or None if the key does not exist.
        """
        bucket = self.hash(key)  # Index of the bucket containing the key-value pair

        for k, v in self.table[
            bucket
        ]:  # Iterate through each key-value pair in the bucket
            if k == key:  # If the key exists in the bucket
                return v  # Return the value

        return None  # If the key does not exist in the bucket, return None

    def get_all(self) -> tuple:
        """
        Gets the value for the given key in the hash table.

        Args:
            keys (list): The keys to get the values for.

        Returns:

        """
        keys = []  # Create an empty list to store the keys
        values = []  # Create an empty list to store the values

        for bucket in self.table:  # Iterate through each bucket in the hash table
            for k, v in bucket:  # Iterate through each key-value pair in the bucket
                keys.append(k)  # Append each key to the keys list
                values.append(v)  # Append each value to the values list

        return keys, values  # Return the keys and values lists as a tuple

    def remove(self, key) -> None:
        """
        Removes the key-value pair for the given key from the hash table.

        Args:
            key: The key to remove the key-value pair for.

        Returns:
            None
        """

        bucket = self.hash(key)  # Index of the bucket containing the key-value pair

        item_to_delete = self.__binary_search__(
            key
        )  # Find the index of the key in the bucket

        if item_to_delete is not None:  # If the key is found in the bucket
            self.table[bucket].pop(
                item_to_delete
            )  # Remove the key-value pair from the bucket

    def __binary_search__(self, key) -> any:
        """
        Perform a binary search on a sorted array to find the target element.

        Args:
            key: The key to find in the hash table.

        Returns:
            int: The index of the target element in the array, or None if the element is not found.

        Notes:
            average time complexity: O(log n)
            worst time complexity: O(log n)
        """
        bucket = self.hash(key)  # Index of the bucket containing the key-value pair

        low = 0  # The low pointer in the search range. Initially, this is the first index.

        high = (
            len(self.table[bucket]) - 1
        )  # The high pointer in the search range. Initially, this is the last index.

        while low <= high:  # Iterate through the bucket to find the key
            mid = (
                low + high
            ) // 2  # Calculate the middle index between the previous search range

            if self.table[bucket][mid] < key:
                low = mid + 1  # Adjust the 'low' pointer
            elif self.table[bucket][mid] > key:
                high = mid - 1  # Adjust the 'high' pointer
            else:  # If the key is found
                return mid  # Return the index of the key

        return None  # If the element was not found in the array. Return None.
