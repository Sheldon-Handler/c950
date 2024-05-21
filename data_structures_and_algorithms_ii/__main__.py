import data_structures_and_algorithms_ii.read_csv_file

data_structures_and_algorithms_ii.packages = (
    data_structures_and_algorithms_ii.read_csv_file.get_packages(
        data_structures_and_algorithms_ii.package_csv_file
    )
)

for i in range(len(data_structures_and_algorithms_ii.packages)):
    print(data_structures_and_algorithms_ii.packages[i].__str__())
