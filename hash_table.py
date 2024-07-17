#  MIT License
#
#  Copyright (c) 2024 Sheldon Handler
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice (including the next paragraph) shall be included in all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

class HashTable:
    """
    A hash table data structure.

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

        Notes:
            time complexity:
                best case = O(n)
                worst case = O(n)
                average case = O(n)
            space complexity:
                best case = O(n)
                worst case = O(n)
                average case = O(n)
        """
        self.table = []

        # Initialize the hash table with empty lists
        for i in range(size):  # O(n) - for loop
            self.table.append([])

    def _hash(self, key) -> int:
        """
        Hashes the given key to a hash value.

        Args:
            key: The key to hash.

        Returns:
            int: The hash value.

        Notes:
            time complexity:
                best case = O(1)
                worst case = O(1)
                average case = O(1)
            space complexity:
                best case = O(1)
                worst case = O(1)
                average case = O(1)
        """
        # Hash the key and return the hash value
        return hash(key) % len(self.table)

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
        hash_value = self._hash(key)

        # Search for the key in the hash table and return the value if found
        for i in self.table[hash_value]:  # O(n) - for loop
            item_key, item_value = i
            if item_key == key:
                return i[1]

        # If the key is not found, return None
        return None

    def get_all(self) -> []:
        """
        Gets all the key-value pairs in the hash table.

        Returns:
            list: A list of key-value pairs in the hash table.

        Notes:
            time complexity:
                best case = O(n^2)
                worst case = O(n^2)
                average case = O(n^2)
            space complexity:
                best case = O(n)
                worst case = O(n)
                average case = O(n)
        """
        items = []

        # Get all the key-value pairs in the hash table
        for i in self.table:  # O(n) - for loop
            for j in i:  # O(n) - for loop
                items.append(j)

        # Sort the key-value pairs by key
        items.sort(key=lambda x: x[0])  # O(n log n) - sort

        return items

    def add(self, key, value) -> None:
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
                worst case = O(1)
                average case = O(1)
            space complexity:
                best case = O(1)
                worst case = O(1)
                average case = O(1)
        """
        hash_value = self._hash(key)

        # Append the key-value pair to the hash table
        self.table[hash_value].append((key, value))

    def update(self, key, value):
        """
        Updates the value for the given key in the hash table.

        Args:
            key: The key to update.
            value: The value to update.

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
        hash_value = self._hash(key)

        # Search for the key in the hash table and update the value if found
        for i in range(len(self.table[hash_value])):  # O(n) - for loop
            if self.table[hash_value][i][0] == key:
                self.table[hash_value][i] = key, value
                return

    def __len__(self) -> int:
        """
        Returns the size of the hash table.

        Returns:
            int: The size of the hash table.

        Notes:
            time complexity:
                best case = O(n)
                worst case = O(n)
                average case = O(n)
            space complexity:
                best case = O(1)
                worst case = O(1)
                average case = O(1)
        """
        size = 0

        for i in self.table:  # O(n) - for loop
            size += len(i)

        return size
