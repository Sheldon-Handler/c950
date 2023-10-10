from package import Package


class HashTable:
    """
    HashTable class to store key-value pairs
    """

    def __init__(self, size: int):
        """
        Initialize HashTable
        :param size: size of the table
        :type size: int
        """
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash(self, key: int):
        """
        Hash function to get index of key
        :param key: key to hash
        :type key: int
        :return: hash of key modulus size of table
        """
        return hash(key) % self.size

    def __insert__(self, key: int, value: Package):
        """
        Insert key-value pair into hash table
        :param key: key of item to insert
        :type key: int
        :param value: value to insert
        :type value: Package
        """
        index = self.hash(key)
        for item in self.table[index]:
            if item[0] == key:
                item[1] = value
                break
        self.table[index].append([key, value])

    def __getitem__(self, key):
        """
        Get item value from key
        :param key: key to get value from
        :return: item value from key if it exists, else raise KeyError
        """
        index = self.hash(key)
        for item in self.table[index]:
            if item[0] == key:
                return item[1]
        raise KeyError(key)

    def __setitem__(self, key: int, value: Package):
        """
        Set item value from key
        :param key: key to set value from
        :type key: int
        :param value: value to set
        :type value: Package
        """
        index = self.hash(key)
        for item in self.table[index]:
            if item[0] == key:
                item[1] = value
                break
        self.table[index].append([key, value])

    def __delitem__(self, key: int):
        """
        Delete item from key
        :param key: key of item to delete
        :type key: int
        """
        index = self.hash(key)
        for item in self.table[index]:
            if item[0] == key:
                self.table[index].remove(item)
                break
            else:
                raise KeyError(key)

