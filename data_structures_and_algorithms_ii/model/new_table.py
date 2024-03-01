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
        bucket = self.table[hash_value]
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key):
        """
        Gets the value for the given key in the hash table.

        Args:
            key: The key to get the value for.

        Returns:
            Any: The value for the given key.

        """

        hash_value = self.hash(key)
        bucket = self.table[hash_value]
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                return bucket[i][1]
        return None
