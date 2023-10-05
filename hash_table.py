import delivery_package

hash_table = []

class HashTable:

    def __init__(self):
        list.__init__()

    def __class_getitem__(cls, item):
        hash_table.__class_getitem__(__item=item)

    def __getitem__(self, index):
        hash_table.__getitem__(__i=index)

    def __setitem__(self, key: int, value: delivery_package):
        hash_table.__setitem__(__i=key, __o=value)

    def __add__(self, __delivery_package: delivery_package.DeliveryPackage):
        hash_table.append(__object=delivery_package)

    def __delitem__(self, __index: int):
        hash_table.__delitem__(__i=__index)

    def __delete__(self, __item: delivery_package.DeliveryPackage):
        hash_table.remove(__value=__item)
