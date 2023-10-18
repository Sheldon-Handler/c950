"""package_csv.py file to store PackageCSV class to store packages in CSV
file."""

# Import csv
import csv
import fileinput

from c950.__init__ import csv_file
# Import Package from package
from package import Package, Status
# Import dataclass from dataclasses
from dataclasses import dataclass


@dataclass
class CsvData:
    """Represents data to be written to a CSV file.

    Attributes:
        headers (List[str]): List of column headers for the CSV file.
        rows (List[List]): List of data rows, where each row is a list of values.

    Example:
        CsvData(
            headers=["Name", "Age", "Email"],
            rows=[
                ["Alice", 30, "alice@example.com"],
                ["Bob", 25, "bob@example.com"],
                ["Charlie", 35, "charlie@example.com"],
            ]
        )
    """

    headers = ["Package ID", "Address", "City", "State", "Postal", "Weight", "Deadline", "Note", "Status"]
    rows: list[list]

    # Method to save CsvData to CSV file
    def save_csv(self):
        """Saves the CsvData to a CSV file.

        Args:
            self (CsvData): The CsvData to save.

        Returns:
            None
        """

        # Create CSV writer
        csv_writer = csv.writer(csv_file, delimiter=",")
        # Write headers to CSV file
        csv_writer.writerow(self.headers)
        # Write rows to CSV file
        csv_writer.writerows(self.rows)

    def load_csv(self):
        """Loads the CsvData from a CSV file.

        Args:
            self (CsvData): The CsvData to load.

        Returns:
            None
        """

        # Create CSV reader
        csv_reader = csv.reader(csv_file, delimiter=",")
        # Skip headers
        next(csv_reader)
        # Read rows from CSV file
        self.rows = list(csv_reader)

    def update_csv(self, package_id, status):
        """Updates the CsvData to a CSV file.

        Args:
            self (CsvData): The CsvData to update.
            package_id (int): The package ID to update.
            status (Status): The status to update.

        Returns:
            None
        """

        # Create CSV reader
        csv_reader = csv.reader(csv_file, delimiter=",")
        # Skip headers
        next(csv_reader)
        # Read rows from CSV file
        self.rows = list(csv_reader)
        # Update status in CSV file
        self.rows[package_id][8] = status
        # Create CSV writer
        csv_writer = csv.writer(csv_file, delimiter=",")
        # Write headers to CSV file
        csv_writer.writerow(self.headers)
        # Write rows to CSV file
        csv_writer.writerows(self.rows)
