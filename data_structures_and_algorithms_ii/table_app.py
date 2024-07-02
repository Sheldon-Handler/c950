import tkinter


class TableApp:
    def __init__(self, parent, data, row_offset, button=None):
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

        # # Add button row
        # self.button = tkinter.Button(
        #     self.frame,
        #     text="Edit",
        #     borderwidth=1,
        #     relief="solid",
        #     bg="lightgreen",
        #     command=button,
        # )
        # self.button.grid(
        #     row=self.rows + 1,
        #     column=0,
        #     sticky="nsew",
        # )
        # self.button.bind("<Button-1>", lambda event: self.button_click())

    def select_row(self, row):
        if self.selected_row is not None:
            if self.selected_row != row:
                for cell in self.cells[self.selected_row]:
                    cell.config(bg="white")
        for cell in self.cells[row]:
            cell.config(bg="lightblue")
        self.selected_row = row

    def button_click(self):
        Button(self.parent, self.button).button_click()


class Button:
    def __init__(self, parent, button):
        self.parent = parent
        self.button = button

    def button_click(self):
        pass


class EditButton(Button):

    def __init__(self, parent, button):
        super().__init__(
            parent, tkinter.Button(parent, text=button, command=self.button_click)
        )

    def button_click(self):
        print("Edit Button Clicked")


class DeliverButton(Button):

    def __init__(self, parent, button):
        super().__init__(
            parent, tkinter.Button(parent, text=button, command=self.button_click)
        )

    def button_click(self):
        print("Deliver Button Clicked")
