"""
package_dao.py contains PackageDAO class to store packages in database.
"""

# Import sqlite3
import sqlite3
# Import Package from package
from package import Package


# PackageDao class
class PackageDao:
    """
    PackageDAO class to store packages in database.
    """

    conn = sqlite3.connect(database="../data/database.db")
    conn.row_factory = sqlite3.Row

    def __init__(self):
        """
        Initialize PackageDAO
        :param self: self to initialize
        :type self: PackageDAO
        """

        # Create tables if they don't exist
        self.conn.executescript("""CREATE TABLE IF NOT EXISTS status (id INT PRIMARY KEY, name VARCHAR);
        UPDATE TABLE SET status (id, name) VALUES (1, "Not Available"), (2, "At Hub"), (3, "En Route"), (4, "Delivered");
        
        CREATE TABLE IF NOT EXISTS package
        (package_id INT PRIMARY KEY,
        address VARCHAR,
        city VARCHAR,
        state VARCHAR,
        zip VARCHAR,
        weight INT,
        deadline VARCHAR,
        note VARCHAR,
        status INT FOREIGN KEY REFERENCES status(id));
        """)

        # Commit changes
        self.conn.commit()

    def __getitem__(self, key):
        """
        Get Package from key. Key is package_id.
        :param key: key to get Package from
        :type key: int
        :return: Package from key
        :rtype: Package
        """

        # Return Package from key
        return self.conn.row_factory.get(key).commit()

    def __setitem__(self, key: int, item: Package):
        """
        Set Package item from key. Key is package_id.
        :param key: key to set item from
        :type key: int
        :param item: Package item to set
        :type item: Package
        """

        # Set Package item from key
        self.conn.row_factory.set(item.package_id, item).commit()

    def __add__(self, item: Package):
        """
        Add Package item to database.
        :param self: self to add item to
        :type self: PackageDAO
        :param item: Package item to add
        :type item: Package
        """

        # Try to add Package item to database
        try:
            # Add Package item to database
            self.conn.row_factory.add(item).commit()
        # If error, raise exception
        except Exception as e:
            # Raise exception
            raise e

    def __delitem__(self, key):
        """
        Delete Package from key. Key is package_id.
        :param self: self to delete Package from
        :type self: PackageDAO
        :param key: key to delete Package from
        :type key: int
        """

        # Delete Package from key. Key is package_id. Commit changes.
        self.conn.row_factory.delete(key).commit()

    def get_all(self):
        """
        Get all Packages from database.
        :param self: self to get all Packages from
        :type self: PackageDAO
        :return: all Packages from database
        :rtype: list
        """

        # Get all Packages from database
        return self.conn.row_factory.fetchall()
