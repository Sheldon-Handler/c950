# Student ID: 007830903
# Name: Sheldon Handler
import hash_table
import package
from package import Package
import sqlite3

conn = sqlite3.connect(database="../data/identifier.sqlite")
conn.execute("CREATE TABLE IF NOT EXISTS package (package_id, address, city, state, postal, weight, deadline, note, status)")

newPackage = Package.__new__(Package)
newPackage.__init__(package_id=2, address="012 Test St", city="Test City", state="NY", postal="01234", weight=21, deadline="12:30", note="g", status="EN_ROUTE")

conn.execute("INSERT INTO package (package_id, address, city, state, postal, weight, deadline, note, status) VALUES ("
             "?, ?, ?, ?, ?, ?, ?, ?, ?)",
                  [newPackage.package_id, newPackage.address, newPackage.city, newPackage.state, newPackage.postal, newPackage.weight, newPackage.deadline,
                   newPackage.note, newPackage.status])
conn.commit()

print(newPackage.__str__())

hashtbl = hash_table.HashTable.__setitem__(hash_table.HashTable.__class__., newPackage.package_id, newPackage)