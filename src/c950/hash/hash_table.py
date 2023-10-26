from functools import reduce


class HashTable:
    """
    A Chained Hash Table with a fixed size of 10.

    This class represents a chained hash table, where each slot in the table can hold multiple key-value pairs in case of collisions. The size of the hash table is fixed at 10.

    Args:
        None

    Attributes:
        size (int): The size of the hash table.
        table (list): The list of buckets to store key-value pairs.
    """

    def __init__(self):
        """
        Initialize the hash table with a fixed size of 10.

        Args:
            None
        """
        self.size = 10
        self.table = [[] for _ in range(self.size)

    def insert(self, key, value):
        """
        Insert a key-value pair into the hash table.

        This method inserts a key-value pair into the hash table, creating sublists if the key is greater than or equal to the size of the hash table. It also handles collisions.

        Args:
            key (int): The key to insert.
            value: The corresponding value to insert.

        Returns:
            None
        """
        if key >= self.size:
            self._resize(key)
        index = key % self.size
        self.table[index].append((key, value))

    def get(self, key):
        """
        Retrieve the value associated with a key from the hash table.

        This method retrieves the value associated with a key from the hash table using the custom_hash method to determine the index.

        Args:
            key (int): The key to retrieve.

        Returns:
            Any: The value associated with the key.

        Raises:
            KeyError: If the key is not found in the hash table.
        """
        index = key % self.size
        for k, value in self.table[index]:
            if k == key:
                return value
        raise KeyError(f"Key '{key}' not found in the hash table")

    def delete(self, key):
        """
        Delete a key-value pair from the hash table.

        This method deletes a key-value pair from the hash table using the custom_hash method to determine the index.

        Args:
            key (int): The key to delete.

        Returns:
            None

        Raises:
            KeyError: If the key is not found in the hash table.
        """
        index = key % self.size
        for pair in self.table[index]:
            if pair[0] == key:
                self.table[index].remove(pair)
                return
        raise KeyError(f"Key '{key}' not found in the hash table")

    def _resize(self, key):
        """
        Resize the hash table to the specified size.

        This method resizes the hash table to the specified size and rehashes the existing key-value pairs into the new table using functional programming style.

        Args:
            key (int): The key that prompted the resizing.

        Returns:
            None
        """
        new_size = max(key, self.size * 2)
        new_table = [[] for _ in range(new_size)]

        rehash = lambda kv, size: new_table[kv[0] % size].append(kv)
        reduce(rehash, reduce(lambda x, y: x + y, self.table), new_size)

        self.size, self.table = new_size, new_table

    def _rehash(self):
        """
        Rehash the hash table.

        This method rehashes the hash table using functional programming style.

        Args:
            None

        Returns:
            None
        """
        rehash = lambda kv, size: self.table[kv[0] % size].append(kv)
        reduce(rehash, reduce(lambda x, y: x + y, self.table), self.size)

# Example usage:
ht = HashTable()
ht.insert(5, "apple")
ht.insert(7, "banana")
ht.insert(15, "cherry")
ht.insert(25, "appel")

print(ht.get(5))  # Output: "apple"
print(ht.get(7))  # Output: "banana"

ht.delete(7)
print(ht.get(7))  # This will raise a KeyError
