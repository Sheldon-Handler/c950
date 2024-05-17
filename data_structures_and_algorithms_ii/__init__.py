import os

addresses = []
distances = []
packages = []
trucks = []

visited_location_indices = {}

number_of_drivers = 2
number_of_trucks = 3
truck_capacity = 16
truck_speed = 18
starting_location = 0

address_csv_file = os.path.realpath("../data/address.csv", strict=True)
distance_csv_file = os.path.realpath("../data/distance.csv", strict=True)
package_csv_file = os.path.realpath("../data/package.csv", strict=True)
