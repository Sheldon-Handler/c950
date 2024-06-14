import tkinter

import data_structures_and_algorithms_ii.read_csv_file

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
root.title("Addresses")
app = GUI.TableApp(root, data_structures_and_algorithms_ii.addresses)

root1 = tkinter.Tk()
root1.title("Packages")
app1 = GUI.TableApp(root1, items)

root.mainloop()
root1.mainloop()
