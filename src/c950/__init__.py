"""__init__.py file to initialize c950.dao package."""
import csv
# Import sqlite3
import sqlite3

# Connect to database
conn = sqlite3.connect(database="../data/database.db")

# Create cursor
cursor = conn.cursor()

# Create package table if it doesn't exist
cursor.execute(
'''
CREATE TABLE IF NOT EXISTS package (
package_id INT PRIMARY KEY,
address VARCHAR,
city VARCHAR,
state VARCHAR,
zip VARCHAR,
weight INT,
deadline VARCHAR,
note VARCHAR,
status INT);
''')

# Commit changes
conn.commit()

# Define csv_file variable
csv_file = "../data/packages.csv"
