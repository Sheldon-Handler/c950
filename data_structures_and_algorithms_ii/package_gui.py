import csv
import tkinter as tk
from tkinter import ttk

import data_structures_and_algorithms_ii


class CSVTableApp:
    """This class creates a table view of a CSV file."""

    def __init__(self, root, csv_file):
        """
        Initializes a CSVTableApp class instance.

        Args:
            root (tk.Tk): The root window.
            csv_file (str): The path to the CSV file.
        """
        self.root = root
        self.root.title("CSV Table Viewer")

        self.tree = ttk.Treeview(root)
        self.tree["columns"] = ()

        with open(csv_file, "r") as file:
            csv_reader = csv.reader(file)
            header = [
                "ID",
                "Address",
                "City",
                "State",
                "Zip",
                "Deadline",
                "Weight Kilo",
                "Special Notes",
            ]
            self.tree["columns"] = header
            self.tree.heading("#0", text="Index")

            for col in header:
                self.tree.heading(col, text=col)
                self.tree.column(col, anchor=tk.CENTER)

            index = 0
            for row in csv_reader:
                self.tree.insert("", index, text=str(index), values=row)
                index += 1

        # Scrollbars
        y_scrollbar = ttk.Scrollbar(root, orient="vertical", command=self.tree.yview)
        y_scrollbar.pack(side="right", fill="y")
        self.tree.configure(yscrollcommand=y_scrollbar.set)

        x_scrollbar = ttk.Scrollbar(root, orient="horizontal", command=self.tree.xview)
        x_scrollbar.pack(side="bottom", fill="x")
        self.tree.configure(xscrollcommand=x_scrollbar.set)

        # Header row
        # self.tree.heading("#0", text="Index")
        for col in header:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor=tk.CENTER)

        self.tree.pack(expand=True, fill=tk.BOTH)


if __name__ == "__main__":
    # Replace 'your_csv_file.csv' with the path to your CSV file
    csv_file_path = data_structures_and_algorithms_ii.package_csv_file

    root = tk.Tk()
    app = CSVTableApp(root, csv_file_path)
    root.mainloop()
