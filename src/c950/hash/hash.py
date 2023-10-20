"""

"""


# Hash class to store objects
class Hash:

    # Constructor
    def __init__(self):
        self.size = 10
        self.table = [None] * self.size

    def hash_function(self, key):
        return key % self.size

hash()