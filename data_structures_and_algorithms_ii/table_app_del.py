import tkinter


class TableApp:
    def __init__(self, parent, data, row_offset, column_offset, button=None):
        self.parent = parent
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0].__dict__)

        # Add frame for the table
        self.frame = tkinter.Frame(parent)
        self.frame.grid(row=row_offset, column=column_offset)

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

        if button is not None:
            # Add button row
            self.button = tkinter.Button(
                self.frame,
                text="Edit",
                borderwidth=1,
                relief="solid",
                bg="lightgreen",
                command=button,
            )
            self.button.grid(
                row=self.rows + 1,
                column=0,
                sticky="nsew",
            )
            self.button.bind("<Button-1>", lambda event: self.button_click())

    def select_row(self, row):
        if self.selected_row is not None:
            if self.selected_row != row:
                for cell in self.cells[self.selected_row]:
                    cell.config(bg="white")
        for cell in self.cells[row]:
            cell.config(bg="lightblue")
        self.selected_row = row

    def button_click(self):
        SearchPackageButton(self.parent, self.button).button_click()


class SearchPackageButton:
    def __init__(self, parent, button):
        self.parent = parent
        self.button = button
        button.config(text="Search")
