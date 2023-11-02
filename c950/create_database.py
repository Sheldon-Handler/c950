import sqlite3


def create_database():
    conn = sqlite3.connect("../data/identifier.sqlite")

    conn.cursor().executescript(
        """
    CREATE TABLE IF NOT EXISTS address (
        id INTEGER PRIMARY KEY,
        address TEXT,
        city TEXT,
        state TEXT,
        zip TEXT
    );
    
    CREATE TABLE IF NOT EXISTS truck (
        id INTEGER PRIMARY KEY,
        packages TEXT,
        miles TEXT,
        time TEXT
        truck_status INTEGER CHECK(truck_status >= 0 AND truck_status <= 3)
    );
    
    CREATE TABLE IF NOT EXISTS packages (
        id INTEGER PRIMARY KEY,
        address TEXT,
        city TEXT,
        state TEXT,
        zip TEXT,
        deadline TIME,
        weight TEXT,
        status TEXT,
        notes TEXT
        delivery_status INTEGER CHECK(delivery_status >= 0 AND delivery_status <= 3),
        truck INTEGER FOREIGN KEY (truck) REFERENCES truck (id)
        delivery_time TIME
    );
    """
    )
