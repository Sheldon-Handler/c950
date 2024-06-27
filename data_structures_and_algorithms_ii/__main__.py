import data_structures_and_algorithms_ii.nearest_neighbor
import data_structures_and_algorithms_ii.read_csv_file
import data_structures_and_algorithms_ii.truck

# Initialize csv files into lists
data_structures_and_algorithms_ii.read_csv_file.init()


# for i in data_structures_and_algorithms_ii.addresses:
#     print(i)

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

package_with_wrong_address = data_structures_and_algorithms_ii.packages.get(9)
package_with_wrong_address.update_address(19)
# corrected_package = data_structures_and_algorithms_ii.package.Package(*package_with_wrong_address)
# corrected_package

for i in data_structures_and_algorithms_ii.addresses:
    print(i.__str__())

items = data_structures_and_algorithms_ii.packages.get_all()

# root = tkinter.Tk()
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

# newGUI = data_structures_and_algorithms_ii.gui.SelectableTableWindow(
#     root, data_structures_and_algorithms_ii.addresses, items
# )
#
# root.mainloop()

new_truck_1 = data_structures_and_algorithms_ii.truck.Truck(
    1,
    "At Hub",
    0,
)
new_truck_2 = data_structures_and_algorithms_ii.truck.Truck(
    2,
    "At Hub",
    0,
)
new_truck_3 = data_structures_and_algorithms_ii.truck.Truck(
    3,
    "At Hub",
    0,
)

print(
    data_structures_and_algorithms_ii.nearest_neighbor.sorted_unvisited_neighbors(
        data_structures_and_algorithms_ii.distances,
        [],
    ),
    "\n",
)

data_structures_and_algorithms_ii.trucks = [new_truck_1, new_truck_2, new_truck_3]


# loading truck 1
data_structures_and_algorithms_ii.trucks[0].load_truck(14)
data_structures_and_algorithms_ii.trucks[0].load_truck(15)
data_structures_and_algorithms_ii.trucks[0].load_truck(19)
data_structures_and_algorithms_ii.trucks[0].load_truck(16)
data_structures_and_algorithms_ii.trucks[0].load_truck(13)
data_structures_and_algorithms_ii.trucks[0].load_truck(20)
data_structures_and_algorithms_ii.trucks[0].load_truck(21)
data_structures_and_algorithms_ii.trucks[0].load_truck(1)
data_structures_and_algorithms_ii.trucks[0].load_truck(29)
data_structures_and_algorithms_ii.trucks[0].load_truck(34)
data_structures_and_algorithms_ii.trucks[0].load_truck(40)
data_structures_and_algorithms_ii.trucks[0].load_truck(4)
data_structures_and_algorithms_ii.trucks[0].load_truck(2)
data_structures_and_algorithms_ii.trucks[0].load_truck(33)
data_structures_and_algorithms_ii.trucks[0].load_truck(17)

truck_1_addresses = [0, 20, 21, 4, 6, 17, 5, 2, 18, 9, 14]

# loading truck 2
data_structures_and_algorithms_ii.trucks[1].load_truck(3)
data_structures_and_algorithms_ii.trucks[1].load_truck(18)
data_structures_and_algorithms_ii.trucks[1].load_truck(36)
data_structures_and_algorithms_ii.trucks[1].load_truck(38)
data_structures_and_algorithms_ii.trucks[1].load_truck(37)
data_structures_and_algorithms_ii.trucks[1].load_truck(5)
data_structures_and_algorithms_ii.trucks[1].load_truck(24)
data_structures_and_algorithms_ii.trucks[1].load_truck(2)
data_structures_and_algorithms_ii.trucks[1].load_truck(33)
data_structures_and_algorithms_ii.trucks[1].load_truck(22)
data_structures_and_algorithms_ii.trucks[1].load_truck(8)
data_structures_and_algorithms_ii.trucks[1].load_truck(30)
data_structures_and_algorithms_ii.trucks[1].load_truck(23)
data_structures_and_algorithms_ii.trucks[1].load_truck(12)

truck_2_addresses = [8, 3, 7, 19, 22, 26, 12, 23, 16]

# loading truck 3
data_structures_and_algorithms_ii.trucks[2].load_truck(6)
data_structures_and_algorithms_ii.trucks[2].load_truck(25)
data_structures_and_algorithms_ii.trucks[2].load_truck(26)
data_structures_and_algorithms_ii.trucks[2].load_truck(28)
data_structures_and_algorithms_ii.trucks[2].load_truck(31)
data_structures_and_algorithms_ii.trucks[2].load_truck(32)
data_structures_and_algorithms_ii.trucks[2].load_truck(9)
data_structures_and_algorithms_ii.trucks[2].load_truck(27)
data_structures_and_algorithms_ii.trucks[2].load_truck(35)
data_structures_and_algorithms_ii.trucks[2].load_truck(7)
data_structures_and_algorithms_ii.trucks[2].load_truck(39)
data_structures_and_algorithms_ii.trucks[2].load_truck(10)
data_structures_and_algorithms_ii.trucks[2].load_truck(11)

truck_3_addresses = [13, 24, 11, 15, 19, 1, 2, 6, 25, 10]

loaded_addresses = truck_1_addresses + truck_2_addresses + truck_3_addresses

print(
    data_structures_and_algorithms_ii.nearest_neighbor.sorted_unvisited_neighbors(
        data_structures_and_algorithms_ii.distances[0],
        loaded_addresses,
    ),
    "\n",
)

print(data_structures_and_algorithms_ii.trucks[0].packages)
print(data_structures_and_algorithms_ii.trucks[1].packages)

addresses = truck_1_addresses + truck_2_addresses
packages_not_loaded = []

print(items)

for i in items:
    if i[1].address not in loaded_addresses:
        packages_not_loaded.append(i)

print(packages_not_loaded)

for i in packages_not_loaded:
    print(i[1].address)


print(
    data_structures_and_algorithms_ii.nearest_neighbor.sorted_unvisited_neighbors(
        data_structures_and_algorithms_ii.distances[0], loaded_addresses
    )
)


loaded_packages = (
    data_structures_and_algorithms_ii.trucks[0].packages
    + data_structures_and_algorithms_ii.trucks[1].packages
    + data_structures_and_algorithms_ii.trucks[2].packages
)

addresses = (
    data_structures_and_algorithms_ii.trucks[0].addresses
    + data_structures_and_algorithms_ii.trucks[1].addresses
    + data_structures_and_algorithms_ii.trucks[2].addresses
)

print(
    data_structures_and_algorithms_ii.nearest_neighbor.sorted_unvisited_neighbors(
        data_structures_and_algorithms_ii.distances[0], addresses
    )
)

print("\n Loaded \n", loaded_packages)

not_yet_loaded = []
for i in items:
    if i[0] not in loaded_packages:
        not_yet_loaded.append(i)

print("\n Not yet loaded: \n", not_yet_loaded)
