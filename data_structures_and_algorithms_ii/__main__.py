import tkinter

import data_structures_and_algorithms_ii.read_csv_file
import data_structures_and_algorithms_ii.table_app

# Initialize csv files into lists
data_structures_and_algorithms_ii.read_csv_file.init()


for i in data_structures_and_algorithms_ii.addresses:
    print(i)

for i in data_structures_and_algorithms_ii.distances:
    print(i)


# data_structures_and_algorithms_ii.packages.update(
#     1,
#     data_structures_and_algorithms_ii.package.Package(
#         1,
#         7,
#         "Salt Lake City",
#         "UT",
#         "84115",
#         "10:30 AM",
#         21,
#         "None",
#         "Delivered",
#     ),
# )
#
items = data_structures_and_algorithms_ii.packages.get_all()


for i in items:
    print(i.__str__())

root = tkinter.Tk()
root.title("Table")

# Add a frame for both tables
frame = tkinter.Frame(root)
frame.grid(row=0, column=0)

edit_button = data_structures_and_algorithms_ii.table_app.EditButton(frame, "Edit")
deliver_button = data_structures_and_algorithms_ii.table_app.Button(frame, "Deliver")

app1 = data_structures_and_algorithms_ii.table_app.TableApp(
    frame, data_structures_and_algorithms_ii.addresses, 0, button=deliver_button
)
app2 = data_structures_and_algorithms_ii.table_app.TableApp(
    frame, items, 1, button=edit_button
)

# button = data_structures_and_algorithms_ii.table_app.EditButton(frame, "Edit")

root.mainloop()
