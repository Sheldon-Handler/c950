"""This module contains the HashTable class to represent a hash table."""

#  MIT License
#
#  Copyright (c) 2023 Sheldon Handler
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice (including the next paragraph) shall be included in all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import node


# HashTable class to store key-value pairs
class HashTable:
    """This class is a custom hash table implementation using chaining to
    resolve collisions. It is used to store key-value pairs.

    Args:
        size (int): The size of the hash table.

    Attributes:
        size (int): The size of the hash table.
        table (list): The hash table, implemented as an array of linked lists.
    """

    def __init__(self, size: int = 10):
        """This method initializes the hash table.

        Args:
            self (HashTable): The hash table self-reference.
            size (int): The number of elements in the hash table.
        """
        self.size = size
        self.table = [None] * size

    def hash(self, key):
        """Hashes the given key to a hash value.

        Args:
            key: The key to hash.

        Returns:
            int: The hash value.
        """

        return key % self.size

    def set(self, key, value):
        """Sets the value for the given key in the hash table.

        Args:
            key: The key to set the value for.
            value: The value to set.

        Returns:
            None
        """

        index = self.hash(key)
        new_node = self.table[index]

        while new_node is not None and new_node.key != key:
            new_node = new_node.next

        if node is None:
            new_node = node.Node(key, value)
            self.table[index] = new_node
        else:
            node.value = value

    def get(self, key):
        """Gets the value for the given key in the hash table.

        Args:
            key: The key to get the value for.

        Returns:
            Any: The value for the given key, or None if the key does not exist.
        """

        index = self.hash(key)
        node = self.table[index]

        while node is not None and node.key != key:
            node = node.next

        if node is None:
            return None
        else:
            return node.value

    def remove(self, key):
        """Removes the key-value pair for the given key from the hash table.

        Args:
            key: The key to remove the key-value pair for.

        Returns:
            Any: The value of the removed key-value pair, or None if the key does not exist.
        """

        index = self.hash(key)
        node = self.table[index]
        previous_node = None

        while node is not None and node.key != key:
            previous_node = node
            node = node.next

        if node is None:
            return None
        else:
            if previous_node is None:
                self.table[index] = node.next
            else:
                previous_node.next = node.next

            return node.value

    def __str__(self):
        """Returns a string representation of the hash table.

        Returns:
            str: A string representation of the hash table.
        """

        string = ""
        for i in range(self.size):
            node = self.table[i]
            while node is not None:
                string += str(node.key) + ":" + str(node.value) + "\n"
                node = node.next

        return string


if __name__ == "__main__":
    h = HashTable()
    h.set(1, "a")
    h.set(2, "b")
    h.set(3, "c")

    print(h.get(1))
    print(h.get(2))
    print(h.get(3))

    h.remove(2)

    print(h.get(2))

    print(h)
