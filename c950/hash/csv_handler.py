"""This module contains the CsvHandler class for handling CSV files."""

#  MIT License
#
#  Copyright (c) <year> <copyright holders>
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice (including the next paragraph) shall be included in all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

import csv


# Method to read CSV file
def read(filename: str) -> list:
    """Read and return the data from the CSV file.

    Reads the data from the CSV file specified during initialization and return it as a
    list of rows. Does not read the header row.

    Returns:
        list: A list of rows, where each row is converted into an instance of cls.

    Example:
        csv_handler = CsvHandler("data.csv")
        data = csv_handler.read_csv()

    References:
        https://docs.python.org/3/library/list.html
        https://docs.python.org/3/library/functions.html#open
        https://docs.python.org/3/library/csv.html
    """

    # Create an empty list of rows to store data
    data_list = []

    # Open file in read mode
    with open(filename, mode="r", newline="") as file:
        # Create csv reader instance for file with excel dialect
        reader = csv.reader(file)
        # Iterate over rows in file
        for row in reader:
            # Append each row to data_list
            data_list.append(row)

        # Return data_list
        return data_list


# Method to write data to the CSV file
def write(filename: str, data: list) -> None:
    """This method writes the data to the CSV file.

    Args:
        filename (str): The name of the CSV file to write to.
        data (list): A list of rows, where each row is represented as an object.

    Example:
        csv_handler = CsvHandler("output.csv")
        data = [[, "Age"], ["Alice", 30], ["Bob", 25]]
        csv_handler.write_csv(data)

    See Also:
        https://docs.python.org/3/library/csv.html
        https://docs.python.org/3/library/list.html
        https://docs.python.org/3/library/functions.html#open
    """

    # Create an empty list of rows to store data
    rows = []

    # Iterate over rows in data
    for row in data:
        # Convert each row object type to list. Append to rows list.
        rows.append(row)

    # open file in write mode
    with open(filename, mode="w", newline="") as file:
        # Create csv writer instance for the file
        writer = csv.writer(file)
        # Write data to file
        writer.writerows(rows)
