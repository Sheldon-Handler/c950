#  MIT License
#
#  Copyright (c) 2024 Sheldon Handler
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice (including the next paragraph) shall be included in all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

class HashTable:
    """
    A hash table class that uses separate chaining to handle collisions.

    Args:
        size (int): The size of the hash table. Defaults to 10.

    Attributes:
        table (list): The hash table.
    """

    def __init__(self, size: int = 10):
        """
        Initializes a hash table object.

        Args:
            size (int): The size of the hash table. Defaults to 10.

        Returns:
            None
        """
        self.table = []

        # Initialize the hash table with empty lists
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
        return hash(key) % len(self.table)  # Hash the key and return the hash value

    def set(self, key, value) -> None:
        """
        Sets the value for the given key in the hash table.

        Args:
            key: The key to set.
            value: The value to set.

        Returns:
            None

        Notes:
            time complexity:
                best case = O(1)
                worst case = O(n)
                average case = O(n)
            space complexity:
                best case = O(1)
                worst case = O(1)
                average case = O(1)
        """
        hash_value = self.hash(key)

        # Check if the key already exists, if so, update the value and return
        for i in self.table[hash_value]:  # O(n) - for loop
            if self.table[hash_value][i][0] == key:
                self.table[hash_value][i][1] = value
                return

        # If the key does not exist, append the key-value pair to the hash table
        self.table[hash_value].append((key, value))

    def get(self, key) -> any:
        """
        Gets the value for the given key in the hash table.

        Args:
            key: The key to get the value for.

        Returns:
            any: The value for the given key.

        Notes:
            time complexity:
                best case = O(1)
                worst case = O(n)
                average case = O(n)
            space complexity:
                best case = O(1)
                worst case = O(1)
                average case = O(1)
        """
        # Hash the key to get the hash value
        hash_value = self.hash(key)

        # Search for the key in the hash table and return the value if found
        for i in self.table[hash_value]:  # O(n) - for loop
            if self.table[hash_value][i][0] == key:
                return self.table[hash_value][i][1]

        # If the key is not found, return None
        return None

    def remove(self, key) -> bool:
        """
        Removes the key-value pair from the hash table.

        Args:
            key: The key of the entry to remove.

        Returns:
            bool: True if the key-value pair was found and removed, False otherwise.

        Notes:
            time complexity:
                best case = O(1)
                worst case = O(n)
                average case = O(n)
            space complexity:
                best case = O(1)
                worst case = O(1)
                average case = O(1)
        """
        # Hash the key to get the hash value
        hash_value = self.hash(key)

        # Search for the key in the hash table and remove the key-value pair if found
        for i in self.table[hash_value]:  # O(n) - for loop
            if self.table[hash_value][i][0] == key:
                self.table[hash_value].pop(i)
                # Return True if the key-value pair was found and removed
                return True

        # Return False if the key-value pair was not found
        return False
