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

    def sampling(self, full_list, length):
        parent_list = list()
        number_of_sublists = (len(full_list) / length) + (len(full_list) % length)
        sublists = []
        for i in range(number_of_sublists):
            for j in range(length):
                if i + j < len(full_list):
                    sublists[i].append(full_list[i + j])
                else:
                    break


        # Return the parent list
        return parent_list