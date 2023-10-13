from collections import namedtuple


class Packagetuple:

    def __init__(self):
        """
        Initialize Packagetuple
        :param self: self to initialize
        :type self: Packagetuple
        """
        self.Packagetuple = namedtuple('Packagetuple', ['package_id', 'address', 'city', 'state', 'postal', 'weight',
                                                        'deadline', 'note', 'status'])
        