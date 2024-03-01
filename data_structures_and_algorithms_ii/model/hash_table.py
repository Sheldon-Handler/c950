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
        """
        hash_value = self.hash(key)

        # Check if the key already exists, if so, update the value and return
        for i in self.table[hash_value]:  # O(n) - for loop
            if self.table[hash_value][i][0] == key:
                self.table[hash_value][i][1] = value
                return

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
        hash_value = self.hash(key)

        for i in self.table[hash_value]:  # O(n) - for loop
            if self.table[hash_value][i][0] == key:
                return self.table[hash_value][i][1]

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
        hash_value = self.hash(key)

        for i in self.table[hash_value]:  # O(n) - for loop
            if self.table[hash_value][i][0] == key:
                self.table[hash_value].pop(i)
                return True

        return False
