"""package_dao.py contains PackageDAO class to store packages in database."""

# Import sqlite3
# Import Package from package
from c950.package import Package


# PackageDao class
class PackageDao:
    """PackageDAO class to store packages in database.

    Methods:
        __init__(self): Constructor for PackageDAO class.
        __getitem__(self, key): Get Package from key. Key is package_id.
        __setitem__(self, key, value): Set Package item from key. Key is package_id.
        __add__(self, other): Add Package item to database.
        __delitem__(self, key): Delete Package from key. Key is package_id.
        get_all(self): Get all Packages from database.
    """

    def __init__(self):
        """Initialize PackageDAO :param self: self to initialize :type self:
        PackageDAO.

        Args:
            self (PackageDAO): self to initialize
        """

        # Create tables if they don't exist
        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS package
        (package_id INT PRIMARY KEY,
        address VARCHAR,
        city VARCHAR,
        state VARCHAR,
        zip VARCHAR,
        weight INT,
        deadline VARCHAR,
        note VARCHAR,
        status INT);
        """)

        # Commit changes
        self.conn.commit()

    def __getitem__(self, key: int) -> Package:
        """Get Package from key.

        Args:
            key (int): key to get Package from

        Returns:
            Package: Package from key
        """

        # Return Package from key
        return c950.dao.__init__.conn.cursor().execute("SELECT * FROM package WHERE package_id = ?", [key]).fetchone()

    def __setitem__(self, key: int, item: Package):
        """

        Args:
            key (int): key to set Package item from
            item (Package): item to set Package item from

        Returns:

        """

        # Set Package item from key
        self.conn.row_factory.set(item.package_id, item).commit()

    def __add__(self, item: Package):
        """Add Package item to database.

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
        """Delete Package from key.

        Key is package_id.
        :param self: self to delete Package from
        :type self: PackageDAO
        :param key: key to delete Package from
        :type key: int
        """

        # Delete Package from key. Key is package_id. Commit changes.
        self.conn.row_factory.delete(key).commit()

    def get_all(self):
        """Get all Packages from database."""

        # Get all Packages from database
        return self.conn.cursor().execute("SELECT * FROM package").fetchall()
