"""package_csv.py file to store PackageCSV class to store packages in CSV
file."""

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

    # Attribute for filename
    filename: str
    # Attribute for header
    header: list[str] = list[""]

    # Constructor
    def __init__(self, filename: str, header: list = list[""]):
        """Initialize the CsvHandler instance.

        Args:
            self (CsvHandler): The CsvHandler instance to initialize.
            filename (str): The name of the CSV file to handle.
            header (list): The header row of the CSV file.

        Returns:
            CsvHandler: A CsvHandler instance for the specified CSV file.

        References:
            https://docs.python.org/3/reference/datamodel.html#object.__init__
        """

        # Set filename attribute
        self.filename = filename
        # Set header attribute
        self.header = header

    # Method to read CSV file
    def read(self) -> list[list]:
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
            reader = csv.reader(csvfile=file, dialect="excel")
            # Skip header row
            next(reader)
            # Iterate over rows in file
            for row in reader:
                # Append row to data
                data_list.append(row)

        # Return data
        return data_list

    # Method to write data to the CSV file
    def write(self, data: list[list], header: list[str] = None) -> None:
        """This method writes the data to the CSV file.

        Args:
            data (list): A list of rows, where each row is represented as a list of values.

        Example:
            csv_handler = CsvHandler("output.csv")
            data = [[, "Age"], ["Alice", 30], ["Bob", 25]]
            csv_handler.write_csv(data)

        See Also:
            https://docs.python.org/3/library/csv.html
            https://docs.python.org/3/library/list.html
            https://docs.python.org/3/library/functions.html#open
        """

        # If header is not None, change the header attribute.
        if header is not None:
            # Set header attribute
            self.header = header

        # open file in write mode
        with open(self.filename, mode="w", newline="") as file:
            # Create csv writer instance for file with excel dialect
            writer = csv.writer(csvfile=file, dialect="excel")
            # Write header row
            writer.writerow(self.header)
            # Write data to file
            writer.writerows(data)


# Example usage:
csv_handler = CsvHandler("data.csv")
data = csv_handler.read()
for row in data:
    print(row)

output_data = [["Name", "Age"], ["Alice", 30], ["Bob", 25]]
output_csv_handler = CsvHandler("output.csv")
output_csv_handler.write(output_data)
