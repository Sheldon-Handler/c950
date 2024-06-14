import tkinter

import data_structures_and_algorithms_ii


class TableApp:
    def __init__(self, parent, data, row_offset):
        self.parent = parent
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0].__dict__)

        # Add frame for the table
        self.frame = tkinter.Frame(parent)
        self.frame.grid(row=0, column=row_offset)

        # Add header row
        headers = list(data[0].__dict__.keys())
        for j, header in enumerate(headers):
            header_label = tkinter.Label(
                self.frame, text=header, borderwidth=1, relief="solid"
            )
            header_label.grid(row=0, column=j, sticky="nsew")

        # Add data rows
        self.selected_row = None
        self.cells = []
        for i in range(self.rows):
            row_cells = []
            for j, key in enumerate(data[i].__dict__):
                cell = tkinter.Label(
                    self.frame,
                    text=getattr(data[i], key),
                    borderwidth=1,
                    relief="solid",
                    bg="white",
                )
                cell.grid(row=i + 1, column=j, sticky="nsew")
                cell.bind("<Button-1>", lambda event, row=i: self.select_row(row))
                row_cells.append(cell)
            self.cells.append(row_cells)

        for i in range(self.rows + 1):  # Adjusted row count to include header row
            self.frame.grid_rowconfigure(i, weight=1)
        for j in range(self.cols):
            self.frame.grid_columnconfigure(j, weight=1)

    def select_row(self, row):
        if self.selected_row is not None:
            if self.selected_row != row:
                for cell in self.cells[self.selected_row]:
                    cell.config(bg="white")
        for cell in self.cells[row]:
            cell.config(bg="lightblue")
        self.selected_row = row


def main():

    root = tkinter.Tk()
    root.title("Table Example")
    app = TableApp(root, data_structures_and_algorithms_ii.addresses, 0)
    root.mainloop()


if __name__ == "__main__":
    main()
