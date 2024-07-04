import datetime
import tkinter

import data_structures_and_algorithms_ii.address
import data_structures_and_algorithms_ii.nearest_neighbor
import data_structures_and_algorithms_ii.read_csv_file
import data_structures_and_algorithms_ii.table_app2
import data_structures_and_algorithms_ii.truck

# Initialize csv files into lists
data_structures_and_algorithms_ii.read_csv_file.init()

# Set arrival times for packages that are delayed on flight
data_structures_and_algorithms_ii.packages.get(6).set_arrival_time(
    datetime.time(hour=9, minute=5)
)
data_structures_and_algorithms_ii.packages.get(25).set_arrival_time(
    datetime.time(hour=9, minute=5)
)
data_structures_and_algorithms_ii.packages.get(28).set_arrival_time(
    datetime.time(hour=9, minute=5)
)
data_structures_and_algorithms_ii.packages.get(32).set_arrival_time(
    datetime.time(hour=9, minute=5)
)


package_with_wrong_address = data_structures_and_algorithms_ii.packages.get(9)
package_with_wrong_address.update_address(19)

items = data_structures_and_algorithms_ii.packages.get_all()

items_list = [i[1] for i in items]

data_structures_and_algorithms_ii.address.load_from_package_list(
    data_structures_and_algorithms_ii.addresses,
    items_list,
)

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
data_structures_and_algorithms_ii.trucks[0].load_truck(34)
data_structures_and_algorithms_ii.trucks[0].load_truck(40)
data_structures_and_algorithms_ii.trucks[0].load_truck(4)
data_structures_and_algorithms_ii.trucks[0].load_truck(30)
data_structures_and_algorithms_ii.trucks[0].load_truck(22)
data_structures_and_algorithms_ii.trucks[0].load_truck(23)


# loading truck 2
data_structures_and_algorithms_ii.trucks[1].load_truck(3)
data_structures_and_algorithms_ii.trucks[1].load_truck(18)
data_structures_and_algorithms_ii.trucks[1].load_truck(36)
data_structures_and_algorithms_ii.trucks[1].load_truck(38)
data_structures_and_algorithms_ii.trucks[1].load_truck(37)
data_structures_and_algorithms_ii.trucks[1].load_truck(24)
data_structures_and_algorithms_ii.trucks[1].load_truck(2)
data_structures_and_algorithms_ii.trucks[1].load_truck(33)
data_structures_and_algorithms_ii.trucks[1].load_truck(8)
data_structures_and_algorithms_ii.trucks[1].load_truck(29)
data_structures_and_algorithms_ii.trucks[1].load_truck(
    6, datetime.time(hour=9, minute=7)
)
data_structures_and_algorithms_ii.trucks[1].load_truck(
    25, datetime.time(hour=9, minute=7)
)
data_structures_and_algorithms_ii.trucks[1].load_truck(26)
data_structures_and_algorithms_ii.trucks[1].load_truck(31)
data_structures_and_algorithms_ii.trucks[1].load_truck(
    32, datetime.time(hour=9, minute=7)
)


# loading truck 3
data_structures_and_algorithms_ii.trucks[2].load_truck(12)
data_structures_and_algorithms_ii.trucks[2].load_truck(17)
data_structures_and_algorithms_ii.trucks[2].load_truck(5)
data_structures_and_algorithms_ii.trucks[2].load_truck(
    28, datetime.time(hour=9, minute=7)
)
data_structures_and_algorithms_ii.trucks[2].load_truck(
    9, datetime.time(hour=10, minute=22)
)
data_structures_and_algorithms_ii.trucks[2].load_truck(27)
data_structures_and_algorithms_ii.trucks[2].load_truck(35)
data_structures_and_algorithms_ii.trucks[2].load_truck(7)
data_structures_and_algorithms_ii.trucks[2].load_truck(39)
data_structures_and_algorithms_ii.trucks[2].load_truck(10)
data_structures_and_algorithms_ii.trucks[2].load_truck(11)


data_structures_and_algorithms_ii.trucks[0].depart_truck(
    datetime.time(hour=8, minute=5)
)
data_structures_and_algorithms_ii.trucks[1].depart_truck(
    datetime.time(hour=9, minute=10)
)
data_structures_and_algorithms_ii.trucks[2].depart_truck(
    datetime.time(hour=10, minute=25)
)

# packages = data_structures_and_algorithms_ii.packages.get_all()
#
# for package in packages:
#     print(package[1]._str())


data_structures_and_algorithms_ii.trucks[0].sort_addresses()
data_structures_and_algorithms_ii.trucks[1].sort_addresses()
data_structures_and_algorithms_ii.trucks[2].sort_addresses()

data_structures_and_algorithms_ii.trucks[0].deliver_all()
data_structures_and_algorithms_ii.trucks[1].deliver_all()
data_structures_and_algorithms_ii.trucks[2].deliver_all()


item_tuples = data_structures_and_algorithms_ii.packages.get_all()
item_values = [i[1] for i in item_tuples]

root = tkinter.Tk()

# root.mainloop()

data_structures_and_algorithms_ii.table_app2.packages_table(item_values)
data_structures_and_algorithms_ii.table_app2.addresses_table(
    data_structures_and_algorithms_ii.addresses
)
