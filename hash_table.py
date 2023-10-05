import csv
import json.tool

import delivery_package

hash_table = []


class HashTable:

    __ht = list.__init__(self=list.__base__)

    def __init__(self):
        HashTable.__ht.__init__()

    def __class_getitem__(cls, item):
        HashTable.__ht.__class_getitem__(__item=item)

    def __getitem__(self, index):
        HashTable.__ht.__getitem__(__i=index)

    def __setitem__(self, key: int, value: delivery_package):
        HashTable.__ht.__setitem__(__i=key, __o=value)

    def __add__(self, __delivery_package: delivery_package.DeliveryPackage):
        HashTable.__ht.append(__object=delivery_package)

    def __delitem__(self, __index: int):
        HashTable.__ht.__delitem__(__i=__index)

    def __delete__(self, __item: delivery_package.DeliveryPackage):
        HashTable.__ht.remove(__value=__item)

    with open("packages.csv", "w") as stream:
        writer = csv.writer(stream)
        for delivery_package.DeliveryPackage in hash_table:
            row = student_to_tuple(student)
            writer.writerow(row)