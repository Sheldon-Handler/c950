#  MIT License
#
#  Copyright (c) 2024 Sheldon Handler
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice (including the next paragraph) shall be included in all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


# from tkinter import Frame, Label, Listbox
#
#
# class SelectableTableWindow:
#
#     def __init__(self, root, data1, data2, table1_header: str, table2_header: str):
#         self.root = root
#         self.root.title("Selectable Tables")
#         self.selected_items = []
#         self.rows1 = len(data1)
#         self.cols1 = len(data1[0].__dict__)
#         self.rows2 = len(data2)
#         self.cols2 = len(data2[0].__dict__)
#
#         # Create frames for each table
#         self.table_frame1 = Frame(self.root)
#         self.table_frame1.pack()
#
#         self.table_frame2 = Frame(self.root)
#         self.table_frame2.pack()
#
#         # Create labels for table headers
#         self.label1 = Label(self.table_frame1, text=table1_header)
#         self.label1.grid(
#             row=self.rows1, column=self.cols1
#         )  # Grid based on column count
#
#         self.label2 = Label(self.table_frame2, text=table2_header)
#         self.label2.grid(
#             row=self.rows2, column=self.cols2
#         )  # Grid based on column count
#
#         # Create listboxes with single selection mode
#         self.listbox1 = Listbox(self.table_frame1, selectmode="browse")
#         self.listbox1.bind("<<ListboxSelect>>", self.on_select1)
#
#         self.listbox1.insert("end", *data1)
#         self.selected_row = None
#
#         for i in range(data1):
#             row_cells = []
#             for j, key in enumerate(data1[i].__dict__):
#                 cell = Label(
#                     self.table_frame1,
#                     text=getattr(data1[i], key),
#                     borderwidth=1,
#                     relief="solid",
#                     bg="white",
#                 )
#                 cell.grid(row=i + 1, column=j, sticky="nsew")
#                 row_cells.append(cell)
#         self.listbox1.grid(row=1, column=0, columnspan=len(data1) // 2, sticky="nsew")
#         # self.listbox1.pack(fill="both", expand=True)
#
#         self.listbox2 = Listbox(self.table_frame2, selectmode="browse")
#         self.listbox2.bind("<<ListboxSelect>>", self.on_select2)
#         self.listbox2.insert("end", *data2)
#         self.listbox2.grid(
#             row=1,
#             column=0,
#             columnspan=len(data2) // 2,
#             sticky="nsew",
#         )
#         # self.listbox2.pack(fill="both", expand=True)
#
#     def on_select1(self, event):
#         # Get the selected item from the listbox1
#         selected_item = self.listbox1.get(self.listbox1.curselection())
#         # Display a message indicating the selection (you can modify this for your needs)
#         print("Selected item in Table 1:", selected_item)
#
#     def on_select2(self, event):
#         # Get the selected item from the listbox2
#         selected_item = self.listbox2.get(self.listbox2.curselection())
#         # Display a message indicating the selection (you can modify this for your needs)
#         print("Selected item in Table 2:", selected_item)
#

# Example usage
# root = Tk()
# data1 = ["Item 1", "Item 2", "Item 3"]
# data2 = ["Value A", "Value B", "Value C"]
# window = SelectableTableWindow(root, data1, data2)
#
# # Run the main loop
# root.mainloop()

from tkinter import Frame, Label, Listbox


class SelectableTableWindow:
    def __init__(self, root, data1, data2):
        self.root = root
        self.root.title("Selectable Tables")
        self.selected_items = {
            1: None,
            2: None,
        }  # Dictionary to store selected row index (table: index)

        # Create frames for each table
        self.table_frame1 = Frame(self.root)
        self.table_frame1.pack(side="left", padx=10, pady=10)

        self.table_frame2 = Frame(self.root)
        self.table_frame2.pack(side="left", padx=10, pady=10)

        self.create_table_headers(self.table_frame1, ["ID", "Name", "Address"])
        self.create_table_headers(
            self.table_frame2,
            [
                "ID",
                "Address ID",
                "City",
                "State",
                "Zip",
                "Delivery Deadline",
                "Weight",
                "Special Notes",
                "Status",
                "Truck ID",
                "Delivery Time",
            ],
        )

        # Create listboxes with entire row selection
        self.listbox1 = Listbox(
            self.table_frame1, selectmode="browse"
        )  # Use browse mode for row selection
        self.listbox1.bind("<<ListboxSelect>>", self.on_select1)
        for row in data1:
            self.listbox1.insert("end", row)  # Insert row as a list
        self.listbox1.grid(row=1, column=0, columnspan=3, sticky="nsew")

        self.listbox2 = Listbox(self.table_frame2, selectmode="browse")
        self.listbox2.bind("<<ListboxSelect>>", self.on_select2)
        for row in data2:
            self.listbox2.insert("end", row)  # Insert row as a list
        self.listbox2.grid(row=1, column=0, columnspan=10, sticky="nsew")

    def create_table_headers(self, table_frame, data):
        # Create labels for each column header
        for col_index, col_name in enumerate(data[0]):
            label = Label(table_frame, text=col_name)
            label.grid(row=0, column=col_index)

    def on_select1(self, event):
        # Get the selected row index from the listbox1
        selected_index = self.listbox1.curselection()[0]
        selected_items = self.listbox1.get(
            selected_index
        )  # Get all items in selected row
        self.selected_items[1] = selected_index  # Store selected row index

    def on_select2(self, event):
        selected_index = self.listbox2.curselection()[0]
        selected_items = self.listbox2.get(selected_index)
        self.selected_items[2] = selected_index

    # ... (similar logic as on_select1, swapping table references)
