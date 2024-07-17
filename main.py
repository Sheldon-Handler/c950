# Student Name: Sheldon Handler
# Student ID: 007830903

import datetime

import __init__
import address
import cmd_input
import read_csv_file
import truck

# Initialize csv files into lists
read_csv_file.init()

# Set arrival times for packages that are delayed on flight
__init__.packages.get(6).set_arrival_time(datetime.time(hour=9, minute=5))
__init__.packages.get(25).set_arrival_time(datetime.time(hour=9, minute=5))
__init__.packages.get(28).set_arrival_time(datetime.time(hour=9, minute=5))
__init__.packages.get(32).set_arrival_time(datetime.time(hour=9, minute=5))

# Set address for package 9 to be wrong and input correct address ID
package_with_wrong_address = __init__.packages.get(9)
wrong_address_update_time = datetime.time(hour=10, minute=20)
package_with_wrong_address.update_address(19, wrong_address_update_time)

items = __init__.packages.get_all()

items_list = [i[1] for i in items]

address.load_from_package_list(
    __init__.addresses,
    items_list,
)

new_truck_1 = truck.Truck(
    1,
    "At Hub",
    0,
)
new_truck_2 = truck.Truck(
    2,
    "At Hub",
    0,
)
new_truck_3 = truck.Truck(
    3,
    "At Hub",
    0,
)

# print(
#     nearest_neighbor.sorted_unvisited_neighbors(
#         __init__.distances,
#         [],
#     ),
#     "\n",
# )

__init__.trucks = [new_truck_1, new_truck_2, new_truck_3]

# loading truck 1
__init__.trucks[0].load_truck(14)
__init__.trucks[0].load_truck(15)
__init__.trucks[0].load_truck(19)
__init__.trucks[0].load_truck(16)
__init__.trucks[0].load_truck(13)
__init__.trucks[0].load_truck(20)
__init__.trucks[0].load_truck(21)
__init__.trucks[0].load_truck(1)
__init__.trucks[0].load_truck(34)
__init__.trucks[0].load_truck(40)
__init__.trucks[0].load_truck(4)
__init__.trucks[0].load_truck(30)
__init__.trucks[0].load_truck(22)
__init__.trucks[0].load_truck(23)

# loading truck 2
__init__.trucks[1].load_truck(3)
__init__.trucks[1].load_truck(18)
__init__.trucks[1].load_truck(36)
__init__.trucks[1].load_truck(38)
__init__.trucks[1].load_truck(37)
__init__.trucks[1].load_truck(24)
__init__.trucks[1].load_truck(2)
__init__.trucks[1].load_truck(33)
__init__.trucks[1].load_truck(8)
__init__.trucks[1].load_truck(29)
__init__.trucks[1].load_truck(6, datetime.time(hour=9, minute=7))
__init__.trucks[1].load_truck(25, datetime.time(hour=9, minute=7))
__init__.trucks[1].load_truck(26)
__init__.trucks[1].load_truck(31)
__init__.trucks[1].load_truck(32, datetime.time(hour=9, minute=7))

# loading truck 3
__init__.trucks[2].load_truck(12)
__init__.trucks[2].load_truck(17)
__init__.trucks[2].load_truck(5)
__init__.trucks[2].load_truck(28, datetime.time(hour=9, minute=7))
__init__.trucks[2].load_truck(9, datetime.time(hour=10, minute=22))
__init__.trucks[2].load_truck(27)
__init__.trucks[2].load_truck(35)
__init__.trucks[2].load_truck(7)
__init__.trucks[2].load_truck(39)
__init__.trucks[2].load_truck(10)
__init__.trucks[2].load_truck(11)

__init__.trucks[0].depart_truck(datetime.time(hour=8, minute=5))
__init__.trucks[1].depart_truck(datetime.time(hour=9, minute=10))
__init__.trucks[2].depart_truck(datetime.time(hour=10, minute=25))

__init__.trucks[0].deliver_all()
__init__.trucks[1].deliver_all()
__init__.trucks[2].deliver_all()

# input_time = cmd_input.prompt_time()
#
# item_tuples = __init__.packages.get_all()
# item_values = [i[1] for i in item_tuples]
#
# package_list_at_time = search_function.package_status_at_time(
#     item_values,
#     input_time,
# )
#
# distance_traveled_list = []
# truck_view_list = []
# total_distance_traveled_at_time = 0
# total_distance_traveled_by_end_of_day = 0
#
# for i in __init__.trucks:  # O(n) - for loop
#     distance_traveled = search_function.distance_traveled(
#         i, package_list_at_time, input_time
#     )  # O(n^2) - function call
#
#     total_distance_traveled_at_time += distance_traveled
#     total_distance_traveled_by_end_of_day += i.distance_traveled
#
#     truck_status = ""
#     if input_time < i.departure_time:
#         truck_status = "At Hub"
#     elif i.return_time > input_time:
#         truck_status = "En Route"
#     elif i.return_time <= input_time:
#         truck_status = "At Hub"
#
#     truck_view = truck.TruckView(
#         i.id, distance_traveled, i.distance_traveled, truck_status
#     )
#     truck_view_list.append(truck_view)

# table_app.main_window(
#     packages_list=package_list_at_time,
#     trucks_view_list=truck_view_list,
#     hour=input_time.hour,
#     minute=input_time.minute,
#     total_distance_at_time=total_distance_traveled_at_time,
#     total_distance_by_end_of_day=total_distance_traveled_by_end_of_day,
# )

cmd_input.prompt_menu()
