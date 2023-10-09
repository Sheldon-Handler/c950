# Student ID: 007830903
# Name: Sheldon Handler
import types

import ctypes

import hash_table
import package
from status import Status

newPackage = package.Package.__new__(package.Package)
newPackage.__init__(address="012 Test St", city="Test City", state="NY", postal="01234", weight=21, deadline="12:30", note="", status=Status.EN_ROUTE)

print(newPackage.__str__())

hash_table.HashTable.__add__(__x=newPackage)