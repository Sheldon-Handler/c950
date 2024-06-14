import tkinter

import data_structures_and_algorithms_ii


class TableApp:
    """
    A table application.

    Attributes:
        root (tkinter.Tk): The root window.
        data (list): The data to display in the table.
        rows (int): The number of rows in the table.
        cols (int): The number of columns in the table.
        table (tkinter.Frame): The table frame.
        selected_row (int): The selected row.
        cells (list): The cells in the table.
    """

    def __init__(self, root, data):
        """
        Initializes a TableApp object instance.

        Args:
            root (): The root window.
            data (): The data to display in the table.

        Returns:
            None

        Notes:
            time complexity: O(n^2)
            space complexity: O(n^2)
        """
        self.root = root
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0].__dict__)

        self.table = tkinter.Frame(root)
        self.table.grid(row=0, column=0)

        # Add header row
        headers = list(data[0].__dict__.keys())
        for j, header in enumerate(headers):  # O(n) - for loop
            header_label = tkinter.Label(
                self.table, text=header, borderwidth=1, relief="solid"
            )
            header_label.grid(row=0, column=j, sticky="nsew")

        # Add data rows
        self.selected_row = None
        self.cells = []
        for i in range(self.rows):  # O(n) - for loop
            row_cells = []
            for j, key in enumerate(data[i].__dict__):  # O(n) - for loop
                cell = tkinter.Label(
                    self.table,
                    text=getattr(data[i], key),
                    borderwidth=1,
                    relief="solid",
                    bg="white",
                )
                cell.grid(row=i + 1, column=j, sticky="nsew")
                cell.bind("<Button-1>", lambda event, row=i: self.select_row(row))
                row_cells.append(cell)
            self.cells.append(row_cells)

        # Configure grid. Adjusted row count to include header row.
        for i in range(self.rows + 1):  # O(n) - for loop
            self.table.grid_rowconfigure(i, weight=1)
        for j in range(self.cols):  # O(n) - for loop
            self.table.grid_columnconfigure(j, weight=1)

    def select_row(self, row):
        if self.selected_row is not None:
            if self.selected_row != row:
                for cell in self.cells[self.selected_row]:  # O(n) - for loop
                    cell.config(bg="white")
        for cell in self.cells[row]:  # O(n) - for loop
            cell.config(bg="lightblue")
        self.selected_row = row


def main():

    root = tkinter.Tk()
    root.title("Table Example")
    app = TableApp(root, data_structures_and_algorithms_ii.addresses)
    root.mainloop()


if __name__ == "__main__":
    main()
