import tkinter

import data_structures_and_algorithms_ii


class TableApp:
    def __init__(self, root, data):
        self.root = root
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0].__dict__)

        self.table = tkinter.Frame(root)
        self.table.grid(row=0, column=0)

        # Add header row
        headers = list(data[0].__dict__.keys())
        for j, header in enumerate(headers):
            header_label = tkinter.Label(
                self.table, text=header, borderwidth=1, relief="solid", width=10
            )
            header_label.grid(row=0, column=j, sticky="nsew")

        # Add data rows
        for i in range(self.rows):
            for j, key in enumerate(data[i].__dict__):
                cell = tkinter.Label(
                    self.table,
                    text=getattr(data[i], key),
                    borderwidth=1,
                    relief="solid",
                    width=10,
                )
                cell.grid(row=i + 1, column=j, sticky="nsew")

        for i in range(self.rows + 1):  # Adjusted row count to include header row
            self.table.grid_rowconfigure(i, weight=1)
        for j in range(self.cols):
            self.table.grid_columnconfigure(j, weight=1)


def main():

    root = tkinter.Tk()
    root.title("Table Example")
    app = TableApp(root, data_structures_and_algorithms_ii.addresses)
    root.mainloop()


if __name__ == "__main__":
    main()
