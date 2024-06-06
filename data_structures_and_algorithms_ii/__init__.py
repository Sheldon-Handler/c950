import os

import data_structures_and_algorithms_ii.hash_table

addresses = []
distances = []
packages = data_structures_and_algorithms_ii.hash_table.HashTable()
trucks = [1, 2, 3]
driver = [1, 2]

visited_location_indices = {}


truck_capacity = 16
truck_speed = 18
starting_location = 0

address_csv_file = os.path.realpath("../data/address.csv", strict=True)
distance_csv_file = os.path.realpath("../data/distance.csv", strict=True)
package_csv_file = os.path.realpath("../data/package.csv", strict=True)
