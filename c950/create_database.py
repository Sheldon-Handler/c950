#  MIT License
#
#  Copyright (c) 2023 Sheldon Handler
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice (including the next paragraph) shall be included in all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

import sqlite3


def create_database() -> None:
    """
    Creates the database and tables if they do not already exist.

    Returns:
        None
    """
    conn = sqlite3.connect("../data/database.sqlite")

    conn.cursor().executescript(
        """    
    CREATE TABLE IF NOT EXISTS address (
        id INTEGER,
        name TEXT,
        address TEXT PRIMARY KEY,
    );
        
    CREATE TABLE IF NOT EXISTS truck (
        id INTEGER PRIMARY KEY,
        truck_status INTEGER CHECK (truck_status >= 0 AND truck_status <= 3),
        address TEXT REFERENCES address (address),
        left_hub TIME,
        packages_assigned: list
        addresses_assigned LIST REFERENCES address (address),
        packages_delivered: list
    );
    
    CREATE TABLE IF NOT EXISTS package (
        id INTEGER PRIMARY KEY,
        address TEXT REFERENCES address (address),
        city TEXT,
        state TEXT,
        zip TEXT,
        delivery_deadline TIME,
        weight_kilo TEXT,
        special_notes TEXT,
        delivery_status INTEGER CHECK (delivery_status >= 0 AND delivery_status <= 3),
        truck INTEGER REFERENCES truck (id),
        loaded_time TIME,
        delivery_time TIME
    );
    """
    )
