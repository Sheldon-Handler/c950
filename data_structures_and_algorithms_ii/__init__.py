import os

addresses = []
distances = []
packages = []
trucks = []

visited_location_indices = {}
unvisited_location_indices = {}

number_of_drivers = 2
number_of_trucks = 3
truck_capacity = 16
truck_speed = 18
starting_location = 0

address_csv_file = os.path.relpath("data/address.csv", start=os.pardir)
distance_csv_file = os.path.relpath("data/distance.csv", start=os.pardir)
package_csv_file = os.path.relpath("data/package.csv", start=os.pardir)
