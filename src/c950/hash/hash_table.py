class ChainingHashTable(list):
    """
    A chaining hash table implemented as a subclass of list.

    Args:
        size (int): The size of the hash table.

    Attributes:
        size (int): The size of the hash table.
    """

    def __init__(self, size):
        """
        Initialize the chaining hash table with a given size.

        Args:
            size (int): The size of the hash table.
        """
        super().__init__([] * size)
        self.size = size

    def _hash_function(self, key):
        """
        Calculate the hash index for a given key.

        Args:
            key: The key to be hashed.

        Returns:
            int: The hash index.
        """
        return hash(key) % self.size

    def insert(self, key, value):
        """
        Insert a key-value pair into the hash table.

        Args:
            key: The key.
            value: The value.
        """
        index = self._hash_function(key)
        for i, (existing_key, existing_value) in enumerate(self[index]):
            if existing_key == key:
                self[index][i] = (key, value)
                break
        else:
            self[index].append((key, value))

    def get(self, key):
        """
        Get the value associated with a key from the hash table.

        Args:
            key: The key.

        Returns:
            The value associated with the key or None if the key is not found.
        """
        index = self._hash_function(key)
        for existing_key, existing_value in self[index]:
            if existing_key == key:
                return existing_value
        return None

    def remove(self, key):
        """
        Remove a key-value pair from the hash table.

        Args:
            key: The key to be removed.
        """
        index = self._hash_function(key)
        self[index] = [(k, v) for k, v in self[index] if k != key]

    def display(self):
        """
        Display the contents of the hash table.
        """
        for i, bucket in enumerate(self):
            if bucket:
                print(f"Bucket {i}: {bucket}")

# Example usage:
hash_table = ChainingHashTable(10)

hash_table.insert("apple", 5)
hash_table.insert("banana", 3)
hash_table.insert("cherry", 8)
hash_table.insert("date", 2)

hash_table.display()

print("Value of 'banana':", hash_table.get("banana"))
print("Value of 'grape':", hash_table.get("grape"))

hash_table.remove("cherry")
hash_table.display()
