import sqlite3

import hash_table
from package import Package


class PackageDAO:

    conn = sqlite3.connect("../data/identifier.sqlite")

    def __init__(self):
        PackageDAO.conn.execute("CREATE TABLE IF NOT EXISTS package (package_id, address, city, state, postal, weight, deadline, note, status)")

    def __add__(self, package: Package):
        PackageDAO.conn.row_factory.insert(package)

    def __delitem__(self, key):
        PackageDAO.conn.row_factory.delete(key)
