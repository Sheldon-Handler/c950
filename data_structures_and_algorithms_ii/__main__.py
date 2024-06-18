import tkinter

import data_structures_and_algorithms_ii.gui
import data_structures_and_algorithms_ii.nearest_neighbor
import data_structures_and_algorithms_ii.read_csv_file
import data_structures_and_algorithms_ii.truck

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
# root.title("Table")
#
# # Add a frame for both tables
# frame = tkinter.Frame(root)
# frame.grid(row=0, column=0)
#
# edit_button = data_structures_and_algorithms_ii.table_app.EditButton(frame, "Edit")
# deliver_button = data_structures_and_algorithms_ii.table_app.DeliverButton(
#     frame, "Deliver"
# )
#
# app1 = data_structures_and_algorithms_ii.table_app.TableApp(
#     frame, data_structures_and_algorithms_ii.addresses, 0, button=deliver_button
# )
# app2 = data_structures_and_algorithms_ii.table_app.TableApp(
#     frame, items, 1, button=edit_button
# )

# button = data_structures_and_algorithms_ii.table_app.EditButton(frame, "Edit")

# root.mainloop()

newGUI = data_structures_and_algorithms_ii.gui.SelectableTableWindow(
    root, data_structures_and_algorithms_ii.addresses, items
)

root.mainloop()

new_truck_0 = data_structures_and_algorithms_ii.truck.Truck(0, "At Hub", 0, [], 0)
new_truck_1 = data_structures_and_algorithms_ii.truck.Truck(1, "At Hub", 0, [], 0)
new_truck_2 = data_structures_and_algorithms_ii.truck.Truck(2, "At Hub", 0, [], 0)

data_structures_and_algorithms_ii.trucks = [new_truck_0, new_truck_1, new_truck_2]

print(
    data_structures_and_algorithms_ii.nearest_neighbor.sorted_unvisited_neighbors(
        data_structures_and_algorithms_ii.distances[0],
        data_structures_and_algorithms_ii.visited_location_indices,
    )
)
