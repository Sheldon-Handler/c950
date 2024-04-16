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
        hash_value = self._hash(key)

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
        hash_value = self._hash(key)

        # Search for the key in the hash table and return the value if found
        for i in self.table[hash_value]:  # O(n) - for loop
            if self.table[hash_value][i][0] == key:
                return self.table[hash_value][i][1]

        # If the key is not found, return None
        return None
