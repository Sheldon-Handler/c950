import data_structures_and_algorithms_ii


def load_package_csv(csv_file: str) -> list:
    """
    Loads the package csv file.

    Returns:
        list: A list of all packages.
    """

    # Declare a list to store packages converted from sublist.
    package_list = []

    # Read the csv file and store it in a variable.
    csvhandler = data_structures_and_algorithms_ii.hash.csv_handler.read(csv_file)

    for row in csvhandler:
        package_list.append(
            data_structures_and_algorithms_ii.model.package.Package(*row)
        )

    data_structures_and_algorithms_ii.global_variables.packages = package_list

    return package_list
