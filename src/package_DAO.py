import sqlite3

import package
from package import Package


class PackageDAO:
    """
    PackageDAO class to store packages in database
    """

    def __init__(self):
        """
        Initialize PackageDAO
        """

        self.conn = sqlite3.connect("../data/database.db")
        self.cursor = self.conn.cursor()

        self.conn.execute("CREATE TABLE IF NOT EXISTS package (package_id INT PRIMARY KEY, address VARCHAR, "
                          "city VARCHAR, state VARCHAR, zip VARCHAR, weight INT, deadline VARCHAR, note VARCHAR, status BLOB)")
        self.conn.commit()

        self.conn.row_factory.register_converter("Package", lambda p: (
            Package(p[0], p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8])))

        self.conn.row_factory.register_adapter(Package, lambda p: (
            p.package_id, p.address, p.city, p.state, p.postal, p.weight, p.deadline, p.note, p.status))

    def __getitem__(self, key):
        """
        Get Package from key. Key is package_id.
        :param key: key to get Package from
        :type key: int
        :return: Package from key
        :rtype: Package
        """

        return self.cursor.fetchone().get(key).commit()

    def __setitem__(self, key: int, item: Package):
        """
        Set Package item from key. Key is package_id.
        :param key: key to set item from
        :type key: int
        :param item: Package item to set
        :type item: Package
        """

        self.conn.row_factory.set(item.package_id, item).commit()

    def __add__(self, item: Package):
        """
        Add Package item to database.
        :param self: self to add item to
        :type self: PackageDAO
        :param item: Package item to add
        :type item: Package
        """

        try:
            self.conn.row_factory.add(item).commit()
        except Exception as e:
            raise e

    def __delitem__(self, key):
        """
        Delete Package from key. Key is package_id.
        :param self: self to delete Package from
        :type self: PackageDAO
        :param key: key to delete Package from
        :type key: int
        """

        self.conn.row_factory.delete(key).commit()

    def get_all(self):
        """
        Get all Packages from database.
        :param self: self to get all Packages from
        :type self: PackageDAO
        :return: all Packages from database
        :rtype: list
        """

        return self.conn.row_factory.fetchall().commit()
