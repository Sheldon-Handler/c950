import data_structures_and_algorithms_ii.read_csv_file


# Initialize csv files into lists
data_structures_and_algorithms_ii.read_csv_file.init()


for i in data_structures_and_algorithms_ii.addresses:
    print(i)

for i in data_structures_and_algorithms_ii.distances:
    print(i)

data_structures_and_algorithms_ii.packages.update(
    1,
    (
        1,
        (
            "123 Main St",
            "Salt Lake City",
            "UT",
            "84115",
            "10:30 AM",
            21,
            "None",
            "At Hub",
            1,
            None,
        ),
        "Salt Lake City",
        "UT",
        "84115",
        "10:30 AM",
        21,
        "None",
        "Delivered",
        1,
        None,
    ),
)
for i in range(1, 8):
    print(data_structures_and_algorithms_ii.packages.get(i)[1].__str__())
