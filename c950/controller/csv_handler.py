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

# Import csv
import csv


# CsvHandler class for handling CSV files.
class CsvHandler:
    """This class Handles reading and writing data in a CSV file.

    Methods:
        __init__(filename): Initialize the CsvHandler instance.
        read(): Read and return the data from the CSV file.
        write(data): Write the data to the CSV file.

    Examples:
        csv_handler = CsvHandler("data.csv")
        data = csv_handler.read()
        for row in data:
            print(row)

        output_data = [["Name", "Age"], ["Alice", 30], ["Bob", 25]]
        output_csv_handler = CsvHandler("output.csv")
        output_csv_handler.write(output_data)

    See Also:
        https://docs.python.org/3/library/csv.html
    """

    # Constructor
    def __init__(self, filename: str):
        """Initialize the CsvHandler instance.

        Args:
            filename (str): The name of the CSV file to handle.
\
        Returns:
            CsvHandler: A CsvHandler instance for the specified CSV file.

        References:
            https://docs.python.org/3/reference/datamodel.html#object.__init__
        """

        # Set filename attribute
        self.filename = filename

    # Method to read CSV file
    def read(self, cls: type) -> list[list]:
        """Read and return the data from the CSV file.

        Reads the data from the CSV file specified during initialization and return it as a
        list of rows. Does not read the header row.

        Args:
            self (CsvHandler): The CsvHandler instance to read from.

        Returns:
            list: A list of rows, where each row is represented as a list of strings.

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
        with open(self.filename, mode="r", newline="") as file:
            # Create csv reader instance for file with excel dialect
            reader = csv.reader(file)
            # Iterate over rows in file
            for row in reader:
                # Append row to data
                data_list.append(row)

        # Return data
        return data_list

    # Method to write data to the CSV file
    def write(self, data: list[list]) -> None:
        """This method writes the data to the CSV file.

        Args:
            data (list[list]): A list of rows, where each row is represented as a list of values.

        Example:
            csv_handler = CsvHandler("output.csv")
            data = [[, "Age"], ["Alice", 30], ["Bob", 25]]
            csv_handler.write_csv(data)

        See Also:
            https://docs.python.org/3/library/csv.html
            https://docs.python.org/3/library/list.html
            https://docs.python.org/3/library/functions.html#open
        """

        # open file in write mode
        with open(self.filename, mode="w", newline="") as file:
            # Create csv writer instance for file with excel dialect
            writer = csv.writer(file)
            # Write data to file
            writer.writerows(data)
