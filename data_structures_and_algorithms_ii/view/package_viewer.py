#  MIT License
#
#  Copyright (c) 2024 Sheldon Handler
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice (including the next paragraph) shall be included in all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

import csv
import tkinter as tk
from tkinter import ttk

import data_structures_and_algorithms_ii
import data_structures_and_algorithms_ii.variables


class CSVTableApp:
    def __init__(self, root, csv_file):
        self.root = root
        self.root.title("CSV Table Viewer")

        self.tree = ttk.Treeview(root)
        self.tree["columns"] = ()

        with open(csv_file, "r") as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader)
            self.tree["columns"] = header
            self.tree.heading("#0", text="Index")

            for col in header:
                self.tree.heading(col, text=col)
                self.tree.column(col, anchor=tk.CENTER)

            index = 1
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
        self.tree.heading("#0", text="Index")
        for col in header:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor=tk.CENTER)

        self.tree.pack(expand=True, fill=tk.BOTH)


if __name__ == "__main__":
    # Replace 'your_csv_file.csv' with the path to your CSV file
    csv_file_path = data_structures_and_algorithms_ii.variables.package_csv_file

    root = tk.Tk()
    app = CSVTableApp(root, csv_file_path)
    root.mainloop()
